def get_line(p1,p2):
    # coefficients for line: Ax + By + C = 0
    A = p1.y - p2.y
    B = p2.x - p1.x
    C = p1.x * p2.y - p2.x * p1.y
    
    return A,B,C

def get_angle(l1, l2):
    # line1 and line2 should be tuple of coefficients A,B,
    a1a2 = l1[0] * l2[0]
    b1b2 = l1[1] * l2[1]
    divider = pow(l1[0] * l1[0] + l1[1] * l1[1], 0.5) * pow(l2[0] * l2[0] + l2[1] * l2[1], 0.5)
    
    return (a1a2 + b1b2) / divider


def get_should_hip_knee_angle(humans, body):
    if 2 in humans[body].body_parts.keys():
        shoulder = humans[body].body_parts[2]
    elif 5 in humans[body].body_parts.keys():
        shoulder = humans[body].body_parts[5]
    else:
        return -1

    if 10 in humans[body].body_parts.keys():
        knee = humans[body].body_parts[10]
    elif 13 in humans[body].body_parts.keys():
        knee = humans[body].body_parts[13]
    else:
        return -1

    if 9 in humans[body].body_parts.keys():
        hip = humans[body].body_parts[9]
    elif 12 in humans[body].body_parts.keys():
        hip = humans[body].body_parts[12]
    else:
        return -1

    l1 = get_line(shoulder, hip)
    l2 = get_line(knee, hip)
    return get_angle(l1,l2)
