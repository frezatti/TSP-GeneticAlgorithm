# This file contains functions for reading TSP data

def read_tsp_coords(filepath):

    coords = []
    reading_coords = False
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: # Skip empty lines
                    continue

                if reading_coords and (line == 'EOF' or any(line.startswith(keyword) for keyword in ['TOUR_SECTION', 'DISPLAY_DATA_SECTION', 'EDGE_WEIGHT_SECTION'])): # Added EDGE_WEIGHT_SECTION just in case
                     reading_coords = False # Stop reading coordinates
                     break # Exit the loop

                if line == 'NODE_COORD_SECTION':
                    reading_coords = True
                    continue # Move to the next line after finding the section header


                if reading_coords:
                    parts = line.split()
                    if len(parts) >= 3:
                        try:
                            x = float(parts[1])
                            y = float(parts[2])
                            coords.append((x, y))
                        except (ValueError, IndexError): # Added IndexError just in case split fails unexpectedly
                            print(f"Warning: Skipping line in NODE_COORD_SECTION due to parsing error: {line}")
                            continue


    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    if reading_coords and not coords:
         print("Warning: NODE_COORD_SECTION found but no valid coordinates were read.")
         return []


    return coords

