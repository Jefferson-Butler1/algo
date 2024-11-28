"""
Jeff Butler, Millen Mistry, Asobo Penn
A quicker gerrymandering algorithm, that beats Striper. Does not find the *most* optimal districts, 
but it will always beat striper given more than 100 rounds, regardless of district size. 
uncomment prints for some fun fancy graphics on districts and islands 
^(most useful when finding tweaking district algorithms)
"""
class QuickMander:
    def __name__(self):
        return "QuickMander"
    
    def gerrymander(self, electorate, party):
        n = electorate.district_size()
        districts = []
        used_voters = set()
        
        # Get multiple possible packed districts, sorted by how well they're packed
        packed_options = self.find_packed_district_options(electorate, party)
        # print(f"Found {len(packed_options)} possible packed districts to try")
        
        # Try each packed district option until we find one that works
        for i, first_district in enumerate(packed_options):
            # print(f"\nTrying packed district option {i+1}")
            party_voters = sum(1 for voter in first_district if electorate.votes[voter] == party)
            # print(f"This district has {party_voters} voters of our party ({(party_voters/n)*100:.1f}%)")
            
            # Start fresh with this option
            districts = [first_district]
            used_voters = set(first_district)
            
            if not self.validate_remaining_voters(electorate, used_voters):
                # print("This packed district creates invalid remaining configuration, trying next option")
                # self._visualize_islands(electorate, used_voters)
                continue
            
            # Try to fill rest of districts
            success = True
            while len(districts) < n:
                # self._print_map(electorate, districts)
                
                start_voter = None
                for j in range(n * n):
                    if j not in used_voters:
                        start_voter = j
                        break
                        
                if start_voter is None:
                    break
                    
                new_district = self.find_contiguous_district(electorate, start_voter, used_voters)
                
                if new_district and len(new_district) == n:
                    districts.append(new_district)
                    used_voters.update(new_district)
                    
                    if not self.validate_remaining_voters(electorate, used_voters):
                        # print(f"\nInvalid districting detected after adding district {len(districts)-1}")
                        # self._visualize_islands(electorate, used_voters)
                        districts.pop()
                        used_voters.difference_update(new_district)
                        success = False
                        break
                else:
                    success = False
                    break
            
            # If we successfully filled all districts, we're done
            if success and len(districts) == n:
                break
            
            # print("Failed to complete the map with this packed district, trying next option")
        
        # self._print_map(electorate, districts)
        
        if len(districts) == n:
            wins_true = electorate.get_wins(districts, True)
            wins_false = electorate.get_wins(districts, False)
            # print(f"District wins - Blue: {wins_true}, Red: {wins_false}")
            # if party:
            #     print(f"Our party (Blue) won {wins_true}/{n} districts ({(wins_true/n)*100:.1f}%)")
            # else:
            #     print(f"Our party (Red) won {wins_false}/{n} districts ({(wins_false/n)*100:.1f}%)")
        
        return districts if len(districts) == n else []
    
    def find_packed_district_options(self, electorate, party):
        """
        Returns a list of possible packed districts, sorted by how well they're packed
        """
        n = electorate.district_size()
        options = []
        
        # Try starting from voters of the OPPOSITE party
        # This way we pack THEM into a single district
        for start_voter in range(n * n):
            if electorate.votes[start_voter] != party:  # Note the change here - looking for opposite party
                district = self.find_contiguous_district(electorate, start_voter, set())
                if district:
                    # Score is how many voters in this district are of the OPPOSITE party
                    score = sum(1 for voter in district if electorate.votes[voter] != party)  # Note the change here
                    options.append((score, district))
        
        # Sort by score in descending order and return just the districts
        return [district for score, district in sorted(options, reverse=True)]

    def find_contiguous_district(self, electorate, start_voter, used_voters):
        """
        Forms a contiguous district starting from the given voter.
        District must contain exactly n voters and can't use already used voters.
        """
        n = electorate.district_size()
        district = {start_voter}
        frontier = {start_voter}
        
        while frontier and len(district) < n:
            current = frontier.pop()
            for neighbor in electorate.graph.neighbors(current):
                if neighbor not in district and neighbor not in used_voters and len(district) < n:
                    district.add(neighbor)
                    frontier.add(neighbor)
        
        return list(district) if len(district) == n else None
    
    def validate_remaining_voters(self, electorate, used_voters):
        """
        Validates that remaining voters can be split into valid districts.
        Returns True if valid, False if invalid.
        """
        n = electorate.district_size()
        remaining = set(range(n * n)) - used_voters
        
        while remaining:
            start = next(iter(remaining))
            island = {start}
            frontier = {start}
            
            while frontier:
                current = frontier.pop()
                for neighbor in electorate.graph.neighbors(current):
                    if neighbor in remaining and neighbor not in island:
                        island.add(neighbor)
                        frontier.add(neighbor)
            
            if len(island) % n != 0:
                return False
            
            remaining -= island
            
        return True
    
    def _visualize_islands(self, electorate, used_voters):
        """
        Helper method to visualize different islands of remaining voters
        """
        pass
        n = electorate.district_size()
        remaining = set(range(n * n)) - used_voters
        islands = []
        
        while remaining:
            start = next(iter(remaining))
            island = {start}
            frontier = {start}
            
            while frontier:
                current = frontier.pop()
                for neighbor in electorate.graph.neighbors(current):
                    if neighbor in remaining and neighbor not in island:
                        island.add(neighbor)
                        frontier.add(neighbor)
            
            islands.append(island)
            remaining -= island
        
        grid = [[None for _ in range(n)] for _ in range(n)]
        
        for voter in used_voters:
            row, col = voter // n, voter % n
            grid[row][col] = 'U'
        
        for i, island in enumerate(islands):
            print(f"Island {i}: size {len(island)}")
            for voter in island:
                row, col = voter // n, voter % n
                grid[row][col] = str(i)
        
        print("\nMap visualization (U=used, numbers=different islands):")
        for row in grid:
            print(' '.join(v if v is not None else '.' for v in row))
        print()
    
    def _print_map(self, electorate, districts):
        size = int(len(electorate.votes) ** 0.5)
        grid = [[None for _ in range(size)] for _ in range(size)]

        for i, district in enumerate(districts):
            for voter in district:
                row, col = voter // size, voter % size
                grid[row][col] = i

        BLUE = "\033[94m"
        RED = "\033[91m"
        WHITE = "\033[97m"
        END = "\033[0m"

        for row in range(size):
            for col in range(size):
                voter = row * size + col
                district = grid[row][col]

                color = BLUE if electorate.votes[voter] else RED
                if district is None:
                    print(color + "□" + END, end=" ")
                else:
                    print(color + str(district) + END, end=" ")
            print()
        print()
