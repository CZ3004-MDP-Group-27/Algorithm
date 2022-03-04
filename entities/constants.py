TURN_PADDING = 4
FOCUS = 25
CAR_DIM = 30
OBS_DIM = 10
MIN_EDGE = float("inf")
TURNING_RAD = 25
DELTA_ST = 5


TR = {
    "90 Turn": (40, 25),
    "Inplace turn": {
        "height": 50,
        "width": 50,
        "st": 15,
        "side": 15
    }

}
INPLACE_TURN_WEIGHT = TR["90 Turn"][0]+TR["90 Turn"][1]+5

WAYPOINT_THETA = {

    0: 270,
    90: 0,
    180: 90,
    270: 180

}

COMMANDS = {
    "F": "FORWARD",
    "B": "BACKWARD",
    "ILEFT": "FORWARD INPLACE LEFT",
    "IRIGHT": "FORWARD INPLACE RIGHT",
    "FTR": "FORWARD TURN RIGHT",
    "FTL": "FORWARD TURN LEFT",
    "BTR": "BACKWARD TURN RIGHT",
    "BTL": "BACKWARD TURN LEFT"
}

ANDROID_COMMANDS = {
    "F": "FORWARD",
    "B": "BACKWARD",
    "ILEFT": "INPLACELEFT",
    "IRIGHT": "INPLACERIGHT",
    "FTR": "FORWARDTURNRIGHT",
    "FTL": "FORWARDTURNLEFT",
    "BTR": "BACKWARDTURNRIGHT",
    "BTL": "BACKWARDTURNLEFT"
}
# WAYPOINT_THETA = {

#     0: 180,
#     90: 270,
#     180: 0,
#     270: 90

# }
