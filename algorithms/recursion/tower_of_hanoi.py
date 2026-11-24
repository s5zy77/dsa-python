def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} -> {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} -> {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


if __name__ == "__main__":
    disks = 3
    print(f"Tower of Hanoi steps for {disks} disks:")
    tower_of_hanoi(disks, "A", "B", "C")