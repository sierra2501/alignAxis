def main () :

    axis = "X"
    face = "LEFT"

    # バウンディングボックスの座標と中心座標
    box_size = xshade.scene().active_shape().bounding_box_size
    box_pos = xshade.scene().active_shape().center_position

    # Z軸に合わせる =============================================================================
    if (axis == "Z"):
        
        if (face == "LEFT"):
            distance = 0 - box_pos[0] - box_size[0]/2
        elif (face == "RIGHT"):
            distance = 0 - box_pos[0] + box_size[0]/2
        elif (face == "CENTER"):
            distance = 0 - box_pos[0]
        else:
            distance = 0

        xshade.scene().move_object(None, None, None, [distance, 0.0, 0.0])

    # X軸に合わせる =============================================================================
    elif (axis == "X"):
        
        if (face == "FRONT"):
            distance = 0 - box_pos[2] - box_size[2]/2
        elif (face == "BACK"):
            distance = 0 - box_pos[2] + box_size[2]/2
        elif (face == "CENTER"):
            distance = 0 - box_pos[2]
        else:
            distance = 0

        xshade.scene().move_object(None, None, None, [0.0, 0.0, distance])

    # Y軸に合わせる =============================================================================
    elif (axis == "Y"):

        if (face == "TOP"):
            distance = 0 - box_pos[1] - box_size[1]/2
        elif (face == "BOTTOM"):
            distance = 0 - box_pos[1] + box_size[1]/2
        elif (face == "CENTER"):
            distance = 0 - box_pos[1]
        else:
            distance = 0

        xshade.scene().move_object(None, None, None, [0.0,  distance, 0.0])


main()