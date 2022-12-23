T = int(input())
for x in range(T):
    N, K = [int(x) for x in input().split(' ')]
    st = input()
    out = []
    far_g = 0
    g_trigger = False
    far_h = 0
    h_trigger = False
    count = 0
    for x in st:
        if g_trigger or far_g < 0:
            far_g += 1
        if h_trigger or far_h < 0:
            far_h += 1

        if x == "G":
            if far_g >= 0:
                g_trigger = True

        elif x == "H":
            if far_h >= 0:
                h_trigger = True

        if far_g == K and g_trigger:
            count += 1
            out.append("G")
            far_g = -K - 1
            g_trigger = False
        elif far_h == K and h_trigger:
            count += 1
            out.append("H")
            far_h = -K - 1
            h_trigger = False
        else:
            out.append(".")

    if h_trigger:
        count += 1
        if out[-1] == '.':
            out[-1] = "H"
        else:
            out[-2] = "H"

    if g_trigger:
        count += 1
        if out[-1] == '.':
            out[-1] = "G"
        else:
            out[-2] = "G"

    print(count)
    print("".join(out))
