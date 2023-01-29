import os
import cv2
from numpy.core.fromnumeric import shape, size
import pytesseract
import numpy as np
import logging
import pandas as pd
import sys


# from django.conf import settings

from pytesseract.pytesseract import image_to_data

# config
custom_config = r'--psm 12 outputbase digits '

# pytesseract.pytesseract.tesseract_cmd = 'D:/Tesseract-OCR/tesseract.exe'
logging.basicConfig(filename='app2.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

column_name = ["HN",
"S_MaxPerfusion", "S_Intervals", "S_ED", "S_ES", "S_EF",
"SM_LADPerfusion", "SSD_LADPerfusion",
"SM_LCXPerfusion", "SSD_LCXPerfusion",
"SM_RCAPerfusion", "SSD_RCAPerfusion",
"SM_TOTPerfusion", "SSD_TOTPerfusion",
"SM_LADWallThickening", "SSD_LADWallThickening",
"SM_LCXWallThickening", "SSD_LCXWallThickening",
"SM_RCAWallThickening", "SSD_RCAWallThickening",
"SM_TOTWallThickening", "SSD_TOTWallThickening",
"SM_LADWallMotion", "SSD_LADWallMotion",
"SM_LCXWallMotion", "SSD_LCXWallMotion",
"SM_RCAWallMotion", "SSD_RCAWallMotion",
"SM_TOTWallMotion", "SSD_TOTWallMotion",
"SE_LADPerfusion", "SE_LCXPerfusion", "SE_RCAPerfusion", "SE_TOTPerfusion",
"SE_LADWallThickening", "SE_LCXWallThickening", "SE_RCAWallThickening", "SE_TOTWallThickening",
"SE_LADWallMotion", "SE_LCXWallMotion", "SE_RCAWallMotion", "SE_TOTWallMotion",
"SSEV_LADPerfusion", "SSEV_LCXPerfusion", "SSEV_RCAPerfusion", "SSEV_TOTPerfusion",
"SSEV_LADWallThickening", "SSEV_LCXWallThickening", "SSEV_RCAWallThickening", "SSEV_TOTWallThickening",
"SSEV_LADWallMotion", "SSEV_LCXWallMotion", "SSEV_RCAWallMotion", "SSEV_TOTWallMotion",
"R_MaxPerfusion", "R_Intervals", "R_ED", "R_ES", "R_EF",
"RM_LADPerfusion", "RSD_LADPerfusion",
"RM_LCXPerfusion", "RSD_LCXPerfusion",
"RM_RCAPerfusion", "RSD_RCAPerfusion",
"RM_TOTPerfusion", "RSD_TOTPerfusion",
"RM_LADWallThickening", "RSD_LADWallThickening",
"RM_LCXWallThickening", "RSD_LCXWallThickening",
"RM_RCAWallThickening", "RSD_RCAWallThickening",
"RM_TOTWallThickening", "RSD_TOTWallThickening",
"RM_LADWallMotion", "RSD_LADWallMotion",
"RM_LCXWallMotion", "RSD_LCXWallMotion",
"RM_RCAWallMotion", "RSD_RCAWallMotion",
"RM_TOTWallMotion", "RSD_TOTWallMotion",
"RE_LADPerfusion", "RE_LCXPerfusion", "RE_RCAPerfusion", "RE_TOTPerfusion",
"RE_LADWallThickening", "RE_LCXWallThickening", "RE_RCAWallThickening", "RE_TOTWallThickening",
"RE_LADWallMotion", "RE_LCXWallMotion", "RE_RCAWallMotion", "RE_TOTWallMotion",
"RSEV_LADPerfusion", "RSEV_LCXPerfusion", "RSEV_RCAPerfusion", "RSEV_TOTPerfusion",
"RSEV_LADWallThickening", "RSEV_LCXWallThickening", "RSEV_RCAWallThickening", "RSEV_TOTWallThickening",
"RSEV_LADWallMotion", "RSEV_LCXWallMotion", "RSEV_RCAWallMotion", "RSEV_TOTWallMotion",
"SSS", "S_STS", "S_SMS",
"SRS", "R_STS", "R_SMS"]

list_result = []
list_confidence = []
df = pd.DataFrame(columns=column_name)
df_conf = pd.DataFrame(columns=column_name)

def dilate(img):
    # dilate
    kernel = np.ones((3,3), np.uint8)
    # conv_img = np.array(img)
    new_im = cv2.dilate(img, kernel, iterations=1)
    return new_im

def erode(img):
    # dilate
    kernel = np.ones((2,2), np.uint8)
    new_im = cv2.erode(img, kernel, iterations=1)
    return new_im

def invert_img(img):
    return cv2.bitwise_not(img)

def convert_to_string(img):
    return pytesseract.image_to_string(img, config=custom_config)

def im_to_bw(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

def resize_img(img):
    return cv2.resize(img, (img.shape[1]*3, img.shape[0]*3))

def extract_text_confidence(img, type_output):
    if(type_output == "number"):
        type = False
    else:
        type = True
    text = convert_to_string(img).split("\n")[0]

    # print(text)
    # print(text.replace('.','',1))
    # print(text.replace('.','',1).replace('-','',1).isdigit())

    try:
        # text เป็นตัวหนังสือแต่ type เป็นตัวเลข
        if((text.replace('.','',1).replace('-','',1).isdigit() == False) & (type == False) | (text == "")):
            text = "-"
            conf_value = 0
            confidence_value = 0
        else:
            img_to_data = image_to_data(img, output_type='data.frame')
            img_data = img_to_data[img_to_data.conf > 10]
            if(img_data.shape[0] == 0):
                if(img_to_data[img_to_data.conf < 10].shape[0] == 1):
                    conf_value = 0
                    confidence_value = 0
                else:
                    text = "-"
                    conf_value = 0
                    confidence_value = 0
            else:
                # print(img_data)
                conf_value = img_data['conf'].values[0]
                # print("conf:", conf_value)
                #confidence value
                # 100-90 = 2 = green
                # 70-89 = 1 = orange
                # 0-69 = 0 = red
                if((conf_value >= 90) & (conf_value <= 100)):
                    confidence_value = 2
                elif((conf_value >= 70) & (conf_value < 90)):
                    confidence_value = 1
                elif((conf_value >= 0) & (conf_value < 70)):
                    confidence_value = 0
            # print(confidence_value)
        print("text:", text, "conf:",conf_value, "conf_level:", confidence_value)
    except Exception as e:
        print("extract data error", e)
    # return text, confidence_value
    return text, conf_value

def severity_scores(im_gray, check_num, version):

    center = int(im_gray.shape[1]/2)

    #version old
    if(version == "old"):
        # block 1 = 0-60, block 2 = 290-350, block 3 = 580-640
        # call & crop img (drop top img)
        print("\\\\ block 1 \\\\")
        j = 0
        for i in range(0,1000,20):
            if(j > 650):
                break
            elif(j > 370 and j < 570):
                print("\\\\ block 3 \\\\")
                j = 580
            elif(j > 80 and j < 100):
                print("\\\\ block 2 \\\\")
                j = 290
            # print(i, j)
            if(check_num == "3" or check_num == "6" ):
                sev = resize_img(im_gray[232+j:250+j+4 , center+410+5:im_gray.shape[1]-45])
            else:
                result_m = im_gray[232+j:250+j+4 , center+330+5:im_gray.shape[1]-127]
                result_m_re = im_to_bw(resize_img(result_m))
                # cv2.imshow('window', im_to_bw(result_m_re))
                # cv2.waitKey(0)

            if(check_num == "1" or check_num == "4" ):
                result_sd = im_gray[232+j:250+j+4 , center+330+61:im_gray.shape[1]-70]
                result_sd_re = resize_img(result_sd)
                # cv2.imshow('window2', im_to_bw(result_sd_re))
                # cv2.waitKey(0)

            if(check_num == "1" or check_num == "4" ):
                mean, mean_conf = extract_text_confidence(result_m_re, "number")
                sd, sd_conf = extract_text_confidence(result_sd_re, "number")

                if(len(mean) >= 2):
                    if(mean[-2] != "." ):
                        print("point of mean is loss")
                        mean = mean[:-1] + "." + mean[-1]
                if(len(sd) >= 2):
                    if(sd[-2] != "."):
                        print("point of sd is loss")
                        sd = sd[:-1] + "." + sd[-1]

                # print("mean: " + mean + " sd: " + sd)
                list_result.append(mean)
                list_result.append(sd)

                list_confidence.append(mean_conf)
                list_confidence.append(sd_conf)

            if(check_num == "2" or check_num == "5" ):
                extent, extent_conf = extract_text_confidence(result_m_re, "number")
                list_result.append(extent)
                list_confidence.append(extent_conf)
                # print("Extent: " + extent)
            elif(check_num == "3" or check_num == "6" ):
                sev_score, sev_conf = extract_text_confidence(sev, "number")
                list_result.append(sev_score)
                list_confidence.append(sev_conf)
                # print("SEV: " + sev_score)

            j += 22
            # print(list_result)
            # break

    #version new
    else:
        print("\\\\ block 1 \\\\")
        j = 0
        for i in range(0,1000,20):
            if(j > 680):
                break
            elif(j > 370 and j < 570):
                print("\n \\\\ block 3 \\\\")
                j = 610
            elif(j >= 80 and j <= 100):
                print("\n \\\\ block 2 \\\\")
                j = 305

            #crop img
            if(check_num == "3" or check_num == "6" ):
                sev = erode(resize_img(im_gray[310+j:330+j , -100:]))
            elif(check_num == "2" or check_num == "5" ):
                extent = erode(resize_img(im_gray[310+j:330+j , center+530:]))
            else:
                im_mean = im_gray
                im_mean[310+j:330+j , center+535:-265] = 255
                mean = erode(resize_img(im_mean[310+j:330+j , center+490:-265]))

                im_sd = im_gray
                sd = erode(resize_img(im_sd[310+j:330+j , -265:-240]))

            # cv2.imshow('window1', sev)
            # cv2.waitKey(0)

            #Convert to string
            if(check_num == "1" or check_num == "4" ):
                mean, mean_conf = extract_text_confidence(mean, "number")
                sd, sd_conf = extract_text_confidence(sd, "number")

                if(len(mean) >= 2):
                    if(mean[-2] != "." ):
                        # print("point of mean is loss")
                        mean = mean[:-1] + "." + mean[-1]
                if(len(sd) >= 2):
                    if(sd[-2] != "."):
                        # print("point of sd is loss")
                        sd = sd[:-1] + "." + sd[-1]

                # print("mean: " + mean + " sd: " + sd)
                list_result.append(mean)
                list_result.append(sd)

                list_confidence.append(mean_conf)
                list_confidence.append(sd_conf)

            if(check_num == "2" or check_num == "5" ):
                extent, extent_conf = extract_text_confidence(extent, "number")
                list_result.append(extent)
                list_confidence.append(extent_conf)
                # print("Extent: " + extent)
            elif(check_num == "3" or check_num == "6" ):
                sev_score, sev_conf = extract_text_confidence(sev, "number")
                if(len(sev_score) > 3):
                    sev_score = sev_score[:3]
                list_result.append(sev_score)
                list_confidence.append(sev_conf)
                # print("SEV: " + sev_score)

            j += 20
            # print(list_result)
            # break

def hn_number(im_gray, filename, version):
    if(version == "old"):
        # call & crop img (drop top img)
        center = int(im_gray.shape[1]/2)

        hn_number = invert_img(im_gray[110:140, center-100:center+100])
    else:
        hn_number = erode(invert_img(im_gray[:40, 150:400]))
        # cv2.imshow('window2', hn_number)
        # cv2.waitKey(0)

    # print("HN:")
    hn_number_str, hn_conf = extract_text_confidence(hn_number, "str")

    if(hn_number_str == filename[:-7]):
        list_result.append(hn_number_str)
        list_confidence.append(hn_conf)
    else:
        hn_number_str = filename[:-7]
        list_result.append(filename[:-7])
        list_confidence.append(hn_conf)
    print(list_result)
    print("HN: ", hn_number_str)

def max_perfusion(im_gray, version):
    center = int(im_gray.shape[1]/2)
    if(version == "old"):
        # call & crop img (drop top img)
        re_img = resize_img(im_gray[185:205, center-110:center-60])
    else:
        max_per = 0
        re_img = resize_img(im_to_bw(im_gray[250:center-530, center-400:center-250]))

    print("Max Perfusion:")
    max_per, max_per_conf = extract_text_confidence(re_img, "number")

    list_result.append(max_per)
    list_confidence.append(max_per_conf)

    return max_per

def left_position(imgray, version):

    if(version == "old"):
        # call & crop img (drop top img)
        im_gray = imgray
        center = int(im_gray.shape[1]/2)

        #ED
        im_gray[215:230, :50] = 0
        im_gray[215:230, 77:100] = 0
        ed1 = im_to_bw(resize_img(invert_img(im_gray[215:230, :center-350])))

        #ES
        im_gray[230:250, :50] = 0
        im_gray[230:250, 77:100] = 0
        es1 = im_to_bw(erode(resize_img(invert_img(im_gray[230:250, :center-350]))))

        #ES
        im_gray[248:265, :35] = 0
        ef1 = im_to_bw(erode(resize_img(invert_img(im_gray[248:265, :center-350]))))

        intervals_img = resize_img(invert_img(im_gray[180:195, :center-350]))
        intervals, intervals_conf = extract_text_confidence(intervals_img, "number")
    else:
        # call & crop img (drop top img)
        im_gray = imgray
        center = int(im_gray.shape[1]/2)

        #ED
        ed1 = (im_gray[95:110, :center-350])

        #ES
        im_gray[230:250, :50] = 0
        im_gray[230:250, 77:100] = 0
        es1 = resize_img(im_gray[110:125, :center-350])

        #ES
        im_gray[248:265, :35] = 0
        ef1 = resize_img(invert_img(im_gray[122:140, :center-350]))

        intervals = "-"

    print("==== ed, es, ef, intervals ====")
    ed, ed_conf = extract_text_confidence(ed1, "number")
    es, es_conf = extract_text_confidence(es1, "number")
    ef, ef_conf = extract_text_confidence(ef1, "number")

    #check_e
    ed = check_e(ed, "ed")
    es = check_e(es, "es")
    intervals = check_e(intervals, "intervals")

    print(ed_conf)
    print(es_conf)
    print(ef_conf)

    list_result.append(intervals)
    list_result.append(ed)
    list_result.append(es)
    list_result.append(ef)

    list_confidence.append(intervals_conf)
    list_confidence.append(ed_conf)
    list_confidence.append(es_conf)
    list_confidence.append(ef_conf)

def check_e(e, whatE):
    # e = ed, es, ef

    if(e.isdigit()):
        result_e = ""
        if(e[-1:] == "."):
            e = e[:-1]
        if(len(e) > 3):
            for i in e:
                if(i.isdigit()):
                    result_e += i
            if(int(result_e[-3:]) < 100):
                e = str(int(result_e[-3:]))
            else:
                e = result_e[-2:]
        if(int(e) > 100 and whatE != "ed"):
            e = e[:-1]
        if(int(e) > 500 and whatE == "ed"):
            e = e[:-1]
    else:
        e = "-"
    return e

def s_scores(im_gray, version):

    center = int(im_gray.shape[1]/2)
    # cv2.imshow('window', im_gray[750:-250 , -50:])
    # cv2.waitKey(0)

    # print()
    if(version == "old"):
        # print(im_gray[750:-300 , center-10:center+150])
        s_s = resize_img(im_to_bw(im_gray[750:-250 , center-10:center+150]))
        # print(s_s)
        sts = resize_img(im_to_bw(im_gray[750:-250 , center+270:center+150+180]))
        sms = resize_img(im_to_bw(im_gray[750:-250 , -50:]))

        print("=== s_s, sts, sms ===")
        s_s_score, s_s_conf = extract_text_confidence(s_s, "number")
        sts_score, sts_conf = extract_text_confidence(sts, "number")
        sms_score, sms_conf = extract_text_confidence(sms, "number")

        # print("x", s_s_score)
        # cv2.imshow('window', im_to_bw(sms))
        # cv2.waitKey(0)
        # sms_new = ""
        # if(len(sms_score) > 1):
        #     for i in sms_score:
        #         print(i)
        #         if(i.isdigit()):
        #             sms_new += i

        # if(s_s_score.isdigit() == False):
        #     s_s_score = "-"
        # else:
        #     s_s_score = s_s_score[-2:]
        # if(sts_score.isdigit() == False):
        #     sts_score = "-"
        # else:
        #     sts_score = sts_score[-2:]
        # if(sms_score.isdigit() == False):
        #     sms_score = "-"
        # else:
        #     sms_score = sms_score[-2:]

        list_result.append(s_s_score)
        list_result.append(sts_score)
        list_result.append(sms_score)

        list_confidence.append(s_s_conf)
        list_confidence.append(sts_conf)
        list_confidence.append(sms_conf)
        # print("S_S: {s_s} STS: {sts} SMS2: {sms}".format(s_s = s_s_score, sts = sts_score, sms = sms_score))
    else:
        s_s = im_to_bw(im_gray[-110:-80 , center+90:center+120])
        sts = resize_img(im_to_bw(resize_img(im_gray[-110:-80 , center+400:center+430])))
        sms = resize_img(im_to_bw(im_gray[750:-300 , -50:]))

        print("=== s_s, sts, sms ===")
        s_s_score, s_s_conf = extract_text_confidence(s_s, "number")
        sts_score, sts_conf = extract_text_confidence(sts, "number")
        sms_score, sms_conf = extract_text_confidence(sms, "number")

        list_result.append(s_s_score)
        list_result.append(sts_score)
        list_result.append(sms_score)

        list_confidence.append(s_s_conf)
        list_confidence.append(sts_conf)
        list_confidence.append(sms_conf)

def call_process(basepath, hn):
    #Call path from directory
    num_file = 1
    error_list = []
    msg_error = ""
    for filename in os.listdir(basepath):
        # filename = "003898-46_07.Tif"
        # print(basepath)
        type_file = filename[-3:]
        print(type_file)
        if(type_file == "Tif"):
            check_file = filename[10:-5]
            print(filename[:-5])
            print(hn+"_"+check_file)
            path = basepath+hn+"_"+check_file+str(num_file)+".Tif"
            print(path)

            # print("check file", check_file)

            if(check_file == "0" and num_file < 9):
                # img is in BGR format if the underlying image is a color image
                img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
                # img = cv2.imread(path)

                version, img = check_version_img(img)
                # print(version)

                # convert to gray
                im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # convert to bw
                im_gray = im_to_bw(im_gray)

                #[top:bottom, left:right]
                im_gray = invert_img(im_gray)

                # check_num = filename[11:-4]
                check_num = str(num_file)
                # print(check_num)
                global list_result
                global list_confidence
                global df
                global df_conf
                try:
                    # severity score
                    if(check_num == "1" or check_num == "4"):
                        if(check_num == "1"):
                            hn_number(im_gray, filename, version)
                            # print("hn >> ",list_result)
                        if(list_result[0] == hn):
                            max_perfusion(im_gray, version)
                            # print("max per >> ",list_result)
                            left_position(im_gray, version)
                            # print("ef ed es >> ",list_result)
                            severity_scores(im_gray, check_num, version)
                            # print("sevirity score >> ",list_result)
                            print("Extract image", check_num, "success.")
                        else:
                            msg_error = "เลขประจำตัวผู้ป่วยกับชื่อไฟล์ไม่ตรงกัน"
                            break
                    # extent score
                    elif(check_num == "2" or check_num == "5"):
                        severity_scores(im_gray, check_num, version)
                        # print("sevirity score >> ",list_result)
                        print("Extract image", check_num, "success.")
                    # extent + sev score
                    elif(check_num == "3" or check_num == "6"):
                        severity_scores(im_gray, check_num, version)
                        # print("sevirity score >> ",list_result)
                        print("Extract image", check_num, "success.")
                    # SRS, SSS etc
                    elif(check_num == "7" or check_num == "8"):
                        s_scores(im_gray, version)
                        print("Extract image", check_num, "success.")
                    # end row in pandas
                    if(check_num == "8"):
                        # add new row
                        print(size(list_confidence))
                        if(size(list_result) == 113):
                            df_new_row = pd.DataFrame(data=np.array([list_result]), columns=column_name)
                            df = pd.concat([df,df_new_row], ignore_index=True)

                            df_conf_new_row = pd.DataFrame(data=np.array([list_confidence]), columns=column_name)
                            df_conf = pd.concat([df_conf,df_conf_new_row], ignore_index=True)
                            list_result = []
                            list_confidence = []
                            print("list_result:", list_result)
                            print("==================================")
                            print("list_confidence:", list_confidence)
                            print("Extract image", check_num, "success.")

                            # print(df)
                        else:
                            error_list.append(list_result)
                            list_result = []
                            list_confidence = []
                    num_file = num_file+1

                except Exception as e:
                    print("Error!, ")
                    print(str(e))
                    logging.error(path + " "+str(e))
                    msg_error = str(e)
                    list_result.append(e)
                    error_list.append(list_result)
                    list_result = []
                # break
            else:
                msg_error = "ไฟล์ไม่ใช่นามสกุล .Tif"
                break

    print("error", error_list)
    # print(msg_error)
    return df, df_conf, msg_error

def crop_img(img):
    img = img[img.shape[0]-1025: , :]
    # print("crop", img.shape[0])
    # cv2.imshow('window2', img)
    # cv2.waitKey(0)
    return img

def check_version_img(img):
    # cv2.imshow('window2', img)
    # cv2.waitKey(0)
    # print(img.shape[0])
    if(img.shape[0] == 1224):
        img = crop_img(img)
    if(img.shape[1] > 1000):
        version = "new"
    else:
        version = "old"
    # print(version)
    return version, img

def main(path, hn):
    # directory = os.path.join(os.path.dirname( __file__ ), path)
    # print(directory)
    # extract_df, confidence_df, msg_error = call_process(directory, hn)
    extract_df, confidence_df, msg_error = call_process(path, hn)
    print(extract_df)
    print(confidence_df)
    return extract_df, confidence_df, msg_error

# df, condf = main("D:\Dropbox\Pond_rMPI_Master\AI_Assistant_HEART_MIBI2\static\ocr\data_for_test\\")