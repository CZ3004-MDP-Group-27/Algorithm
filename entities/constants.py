TURN_PADDING = 4
FOCUS = 20
CAR_DIM = 30
OBS_DIM = 10
MIN_EDGE = float("inf")
TURNING_RAD = 25
DELTA_ST = 1


TR = {
    "90 Turn": (35, 25),
    "Inplace turn": (20,20)
}
INPLACE_TURN_WEIGHT = TR["90 Turn"][0]+TR["90 Turn"][1]+5

# WAYPOINT_THETA = {

#     0: 270,
#     90: 0,
#     180: 90,
#     270: 180

# }
WAYPOINT_THETA = {

    0: 180,
    90: 270,
    180: 0,
    270: 90

}