from queue import Queue
def water_jug(x,y,z):
    if x+y < z:
        return False

    visited = set()
    q = Queue()
    directions = (x, -x, y, -y)
    q.put(0)
    visited.add(0)
    while not q.empty():
        current = q.get()
        for direction in directions:
            total=current+direction
            if total==z:
                return True
            if total<0 or total>x+y:
                continue
            if total not in visited:
                q.put(total)
                visited.add(total)
    return False

if __name__ == "__main__":
    j1=int(input("Enter the capacity of jug1:"))
    j2 = int(input("Enter the capacity of jug2:"))
    measure = int(input("Enter the capacity to measure:"))
    print(water_jug(j1,j2,measure))
