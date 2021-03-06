def main () :

    axis = TARGET_AXIS
    face = TARGET_FACE
    coord = TARGET_COORD
    flag = TARGET_FLAG


    if (flag == "false"):
        alignAxis(axis, face, coord)
        return
    elif (flag == "true" and xshade.scene().active_shape().has_son == True):

        xshade.scene().active_shape().son.bro.activate()
        alignAxis(axis, face, coord)

        while(xshade.scene().active_shape().has_bro):
            xshade.scene().active_shape().bro.activate()
            alignAxis(axis, face, coord)

        xshade.scene().active_shape().dad.activate()


def alignAxis (axis, face, coord):

    # バウンディングボックスの座標と中心座標
    box_size = xshade.scene().active_shape().bounding_box_size
    box_pos = xshade.scene().active_shape().center_position

    # Z軸に合わせる =============================================================================
    if (axis == "Z"):
        if (face == "FRONT"):
            distance = coord - box_pos[2] - box_size[2]/2
        elif (face == "BACK"):
            distance = coord - box_pos[2] + box_size[2]/2
        elif (face == "CENTER"):
            distance = coord - box_pos[2]
        else:
            distance = coord

        xshade.scene().move_object(None, None, None, [0.0, 0.0, distance])

    # X軸に合わせる =============================================================================
    elif (axis == "X"):
        
        if (face == "LEFT"):
            distance = coord - box_pos[0] + box_size[0]/2
        elif (face == "RIGHT"):
            distance = coord - box_pos[0] - box_size[0]/2
        elif (face == "CENTER"):
            distance = coord - box_pos[0]
        else:
            distance = coord

        xshade.scene().move_object(None, None, None, [distance, 0.0, 0.0])

    # Y軸に合わせる =============================================================================
    elif (axis == "Y"):

        if (face == "TOP"):
            distance = coord - box_pos[1] - box_size[1]/2
        elif (face == "BOTTOM"):
            distance = coord - box_pos[1] + box_size[1]/2
        elif (face == "CENTER"):
            distance = coord - box_pos[1]
        else:
            distance = coord

        xshade.scene().move_object(None, None, None, [0.0,  distance, 0.0])


main()