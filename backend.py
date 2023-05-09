import cv2
import numpy as np

global categories
categories = {}


def load_files(filenames):
    # Step 1 of patent
    # Loading the image
    for file in filenames:
        program(file)
    return categories


def program(file):
    # read file
    img = cv2.imread(file)

    # initialize user definable numbers
    udn_one = 20
    udn_two = 50
    udn_three = 1000
    udn_four = 10

    char_count = 0

    # resize the image
    new_width = 900
    new_height = 900
    dim = (new_width, new_height)
    # img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # preprocess the image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying 7x7 Gaussian Blur
    blurred = cv2.GaussianBlur(gray_img, (1, 1), 0)

    # Applying threshold
    # threshold = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    threshold = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Step 2 of patent
    # Apply the Component analysis function
    analysis = cv2.connectedComponentsWithStats(threshold, 4, cv2.CV_32S)
    (totalLabels, label_ids, values, centroid) = analysis

    # Initialize a new image to
    # store all the output components
    output = np.zeros(gray_img.shape, dtype="uint8")

    suspected_chars = []
    f_suspected_chars = []
    exact_matches = []
    global categories
    # counted = count_elements(range(1, totalLabels))

    # Loop through each component
    for i in range(1, totalLabels):

        # Area of the component
        area = values[i, cv2.CC_STAT_AREA]

        if (area > 14) and (area < 400):

            # Create a new image for bounding boxes
            new_img = img.copy()

            # Step 4 of patent
            # Now extract the coordinate points
            x1 = values[i, cv2.CC_STAT_LEFT]
            y1 = values[i, cv2.CC_STAT_TOP]
            w = values[i, cv2.CC_STAT_WIDTH]
            h = values[i, cv2.CC_STAT_HEIGHT]

            # Coordinate of the bounding box
            pt1 = (x1, y1)
            pt2 = (x1 + w, y1 + h)
            (X, Y) = centroid[i]

            # Step 3 of patent
            # Bounding boxes for each component
            cv2.rectangle(new_img, pt1, pt2, (0, 255, 0), 3)
            cv2.circle(new_img, (int(X), int(Y)), 4, (0, 0, 255), -1)

            # Create a new array to show individual component
            component = np.zeros(gray_img.shape, dtype="uint8")
            componentMask = (label_ids == i).astype("uint8") * 255

            # Apply the mask using the bitwise operator
            component = cv2.bitwise_or(component, componentMask)
            output = cv2.bitwise_or(output, componentMask)

            # Step 5 of patent
            # find number of pixels
            num_pixels = np.sum(component == 255)

            # find horizontal run
            run_count = 0
            longest_run = 0
            # print (np.argwhere(component == 255))
            new_arr = np.argwhere(component == 255)
            num_rows, num_cols = new_arr.shape
            for x in range(num_rows):
                curr_x_coor = new_arr[x][0]
                occurence = (new_arr == curr_x_coor).sum()
                if occurence > longest_run:
                    longest_run = occurence


            # Step 6 of patent
            if (num_pixels > udn_two) and (num_pixels < udn_three):
                # f_suspected_chars.append(f_component(i, w, h, num_pixels))
                suspected_chars.append(num_pixels)
                # suspected_chars.append(longest_run)
                char_count = char_count + 1
                # print("Component " + str(i) + " - width: " + str(w) + " height: " + str(h) + " num pixels: " + str(num_pixels) + " max horizontal run: " + str(longest_run))
                exact_matches.append(
                    "w=" + str(w) + " h=" + str(h) + " p=" + str(num_pixels) + " mhr=" + str(longest_run))
                f_suspected_chars.append(f_component(i, w, h, num_pixels, longest_run))

            # Show the final images
            # cv2.imshow("Thresh", threshold)
           # cv2.imshow("Image", new_img)
          #  cv2.imshow("Individual Component", component)
          #  cv2.imshow("Filtered Components", output)
            # cv2.waitKey(0)

    counted = count_elements(suspected_chars)
    fcounted = count_elements(f_suspected_chars)
    matches = countOccurrence(exact_matches)

    print("total suspected characters: " + str(char_count))
    if (char_count <= udn_one):
        # print("unknown")
        categories[file] = 'Unknown'
    else:
        # Step 31 of patent
        match_score = 0
        match_sum = 0
        for i in matches:
            if (matches[i] > 1):
                match_sum = match_sum + matches[i]
        match_score = match_sum / char_count
        print("match score: " + str(match_score))

        # Step 32 of patent
        sum_ratios = 0
        num_results = 0
        for x in range(len(f_suspected_chars)):
            if (f_suspected_chars[x].maxhr > udn_four):
                num_results = num_results + 1
                # Step 33 of patent
                ratio = f_suspected_chars[x].maxhr / f_suspected_chars[x].width
                # Step 34 of patent
                sum_ratios = sum_ratios + ratio
        max_run_ratio = sum_ratios / num_results
        print("max run ratio: " + str(max_run_ratio))

        # Steps 36-41 of patent
        if (match_score > 0.5):
            # print("machine printed")
            categories[file] = 'Machine-printed'
        elif (max_run_ratio > 0.8):
            # print("machine printed")
            categories[file] = 'Machine-printed'
        elif (max_run_ratio < 0.5):
            #  print("handwritten")
            categories[file] = 'Handwritten'
        elif (max_run_ratio > 0.7 and match_score > 0.05):
            #  print("machine printed")
            categories[file]: 'Machine-printed'
        elif (match_score < 0.1):
            #  print("handwritten")
            categories[file] = 'Handwritten'
        elif (match_score > 0.4):
            # print("machine printed")
            categories[file] = 'Machine-printed'

    print(categories)


def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist


def countOccurrence(a):
    k = {}
    for j in a:
        if j in k:
            k[j] += 1
        else:
            k[j] = 1
    return k


class f_component:
    def __init__(self, name, width, height, pcount, maxhr):
        self.name = name
        self.width = width
        self.height = height
        self.pcount = pcount
        self.maxhr = maxhr
