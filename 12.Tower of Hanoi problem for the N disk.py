def tower_of_hanoi(n, start, end, aux):
    if n == 1:
        print("Move disk 1 from start", start, "to end", end)
        return
    tower_of_hanoi(n-1, start, aux, end)
    print("Move disk", n, "from start", start, "to end", end)
    tower_of_hanoi(n-1, aux, end, start)


no = 4
tower_of_hanoi(no, 'A', 'B', 'C')
