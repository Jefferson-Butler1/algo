class Gerrymander:
    """A class that implements district optimization algorithms for electoral mapping.
    
    This implementation ensures districts are contiguous and of equal size while
    attempting to maximize representation for a given party through district arrangement.
    """
    
    def gerrymander(self, electorate, party):
        """Attempts to create district boundaries that maximize wins for the given party.
        
        Args:
            electorate: An Electorate object containing voter graph and preferences
            party: The party ID to optimize districts for
        
        Returns:
            list: A list of districts (each district is a list of voter IDs)
            
        Raises:
            ValueError: If no valid district arrangement can be found that ensures victory
        """
        # Initialize core parameters
        district_size = electorate.district_size()
        total_voters = electorate.number_of_voters()
        districts_needed_for_majority = (district_size // 2) + 1
        
        def is_district_contiguous(district):
            """Verifies that all voters in a district are connected.
            
            Uses depth-first search to ensure all voters in the district can be reached
            from any starting point.
            
            Args:
                district (set): Set of voter IDs representing a district
                
            Returns:
                bool: True if district is contiguous, False otherwise
            """
            visited = set()
            
            def depth_first_search(voter):
                if voter not in visited:
                    visited.add(voter)
                    for neighbor in electorate.graph.neighbors(voter):
                        if neighbor in district:
                            depth_first_search(neighbor)
            
            # Start DFS from any voter in the district
            start_voter = next(iter(district))
            depth_first_search(start_voter)
            
            return len(visited) == len(district)
        
        def find_districts(current_districts, available_voters, districts_won):
            """Recursively builds valid district arrangements using backtracking.
            
            Args:
                current_districts (list): List of already formed districts
                available_voters (list): List of voters not yet assigned to districts
                districts_won (int): Number of districts currently won by target party
                
            Returns:
                list or None: Valid district arrangement if found, None otherwise
            """
            # Check if we've successfully assigned all districts
            if len(current_districts) == district_size:
                return current_districts if districts_won >= districts_needed_for_majority else None
            
            # Try to form a new district starting with each available voter
            for voter in available_voters:
                # Initialize new district with starting voter
                new_district = {voter}
                growth_queue = [voter]
                
                # Grow district by adding adjacent voters
                while growth_queue and len(new_district) < district_size:
                    current_voter = growth_queue.pop()
                    for neighbor in electorate.graph.neighbors(current_voter):
                        if neighbor in available_voters and neighbor not in new_district:
                            new_district.add(neighbor)
                            growth_queue.append(neighbor)
                
                # Check if district meets size and contiguity requirements
                if len(new_district) == district_size and is_district_contiguous(new_district):
                    # Calculate remaining voters and check if party wins this district
                    remaining_voters = [v for v in available_voters if v not in new_district]
                    party_votes = sum(1 for v in new_district if electorate.votes[v] == party)
                    is_district_won = party_votes > district_size // 2
                    
                    # Recursively try to complete the districting
                    result = find_districts(
                        current_districts + [list(new_district)],
                        remaining_voters,
                        districts_won + (1 if is_district_won else 0)
                    )
                    
                    if result:
                        return result
            
            # No valid arrangement found from this configuration
            return None
        
        # Start the districting process with all voters available
        initial_voters = list(range(total_voters))
        final_districts = find_districts([], initial_voters, 0)
        
        if not final_districts:
            raise ValueError("No Possible Win Condition")
            
        return final_districts
