def my_bilinear(src, scale=None, output_shape=None):

    """
    함수 인자 정보
    src: 입력 영상
    scale: 튜플 형태로 각각 높이와 너비에 대한 축소 또는 확대 시킬 값
    예를들어, scale = (h_scale, w_scale)
    """

    src = src.astype(np.float32)
    (h, w) = src.shape

    # scale이 지정된 경우
    if scale is not None:
        h_scale, w_scale = scale
        h_dst = int(h * h_scale + 0.5)
        w_dst = int(w * w_scale + 0.5)

    # scale이 지정 안되고 구체적인 dst 크기가 지정된 경우
    else:
        h_dst, w_dst = output_shape
        h_scale = h_dst / h
        w_scale = w_dst / w

    dst = np.zeros((h_dst, w_dst), dtype=np.float32)

    for row in range(h_dst):
        for col in range(w_dst):

            ######################################
            # TODO Bilinear interpolation 직접 구현
            ######################################

            y = row / h_scale
            x = col / w_scale

            m = int(np.floor(y)) 
            n = int(np.floor(x))

            if m < h-1 and n < w-1: 
                t = y - m
                s = x - n

                dst[row, col] = (1-s) * (1-t) * src[m, n] + s *(1-t) *src[m, n+1] + (1-s) * t *src[m+1, n] + s * t *src[m+1, n+1]


    dst = np.clip(np.round(dst), 0, 255).astype(np.uint8) # 반올림
    return dst