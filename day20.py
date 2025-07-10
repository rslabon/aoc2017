lines = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
""".strip().splitlines()

lines = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0> 
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
""".strip().splitlines()

with open("./resources/day20.txt") as f:
    lines = f.read().strip().splitlines()

particles = []
for line in lines:
    p, v, a = line.split(", ")
    px, py, pz = [int(i) for i in p.replace("p=<", "").replace(">", "").split(",")]
    vx, vy, vz = [int(i) for i in v.replace("v=<", "").replace(">", "").split(",")]
    ax, ay, az = [int(i) for i in a.replace("a=<", "").replace(">", "").split(",")]
    particles.append([len(particles), [px, py, pz], [vx, vy, vz], [ax, ay, az], 0])


def manhatan(p):
    return abs(p[0]) + abs(p[1]) + abs(p[2])


def part1(particles):
    min_id = None
    while True:
        for (id, p, v, a, c) in particles:
            px, py, pz = p
            vx, vy, vz = v
            ax, ay, az = a
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[id] = [id, [px, py, pz], [vx, vy, vz], [ax, ay, az], c]

        closest = min(particles, key=lambda x: manhatan(x[1]))
        closest[4] += 1
        if closest[4] == 500:
            min_id = closest[0]
            break

    print(min_id)


def part2(particles):
    stable = 1000
    while stable > 0:
        for i, (id, p, v, a, c) in enumerate(particles):
            px, py, pz = p
            vx, vy, vz = v
            ax, ay, az = a
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[i] = [id, [px, py, pz], [vx, vy, vz], [ax, ay, az], c]

        collisions = dict()
        destroyed = set()
        for (id, p, _, _, _) in particles:
            c = collisions.get(tuple(p), set())
            c.add(id)
            collisions[tuple(p)] = c
            if len(c) > 1:
                destroyed |= c

        if destroyed:
            stable = 500
            particles = [particle for particle in particles if particle[0] not in destroyed]
        else:
            stable -= 1

    print(len(particles))


part1(particles[:])
part2(particles[:])
