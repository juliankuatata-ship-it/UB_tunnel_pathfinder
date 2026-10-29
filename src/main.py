from .algorithm import bfs_shortest_path
from .tunnelpaths import tunnel_paths

if __name__ == "__main__":
    print("=== UB Campus Tunnel Navigation System ===")
    print("Available buildings:")
    for building in sorted(tunnel_paths.keys()):
        print(f" - {building}")
    
    start_building = input("\nEnter starting building: ").strip()
    target_building = input("Enter destination building: ").strip()
    
    if start_building not in tunnel_paths or target_building not in tunnel_paths:
        print("\nError: One or both building names are invalid. Check spelling against the list above.")
    elif start_building == target_building:
        print("\nYou are already at the destination building.") 
    else:
        path = bfs_shortest_path(tunnel_paths, start_building, target_building)
        if path:
            print(f"\nShortest path ({len(path) - 1} steps):")
            print(" -> ".join(path))
        else:
            print(f"\nNo path found between {start_building} and {target_building}.")