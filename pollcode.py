# -*-coding:utf-8-*-
# Author: Liu Jing
# Data: 2020  11:20
# File Name: pollcode
import os
import time
import string
import random
import tkinter
import qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
from tkinter import *
from string import digits
from tkinter import messagebox

root = tkinter.Tk()


def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)


def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


def inputbox(showstr, showorder, length):
    instr = input(showstr)
    if len(instr) == 0:
        print('\033[1;31;40m  输入为空，请重新输入： \33[0m')
        return 0
    else:
        if showorder == 1:
            if str.isdigit(str(showorder)):
                if instr == 0:
                    print('\033[1;31;40m  输入为0，请重新输入！\033[0m')
                    return 0
                else:
                    return instr
            else:
                print('\033[1;31;40m  输入1非法，请重新输入！ \033[0m')
                return 0
        elif showorder == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print('\033[1;31;40m  必须输入' + str(length) + '个字母，请重新输入！\033[0m')
                    return 0
                else:
                    return instr
            else:
                print('\033[1;31;40m  输入2非法，请重新输入！ \033[0m')
                return 0
        elif showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print('\033[1;31;40m  必须输入' + str(length) + '个数字，请重新输入！\033[0m')
                    return 0
                else:
                    return instr
            else:
                print('\033[1;31;40m  输入3非法，请重新输入！\033[0m')
                return 0


def wfile(sstr, sfile, typels, smsg, datapath):
    mkdir(datapath)
    datafile = datapath + '\\' + sfile
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ''
    wdata = ''
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')
        wdata = wdata.replace(''''','').replace(''''', '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print('\033[1;31m' + pdata + '\033[0m')
    if typels != 'no':
        messagebox.showinfo('提示', smsg + str(len(sstr)) + '\n防伪码文件存放位置：' + datapath)
        root.withdraw()


number = '123456789'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
allis = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
i = 0
randstr = []
fourth = []
fifth = []
randfir = ''
randsec = ''
randthr = ''
str_one = ''
strone = ''
strtwo = ''
nextcard = ''
userput = ''
nres_letter = ''


def mainmenu():
    print('\033[1;35m'
          '*****************************************************************''\n'
          '                          企业编码生成系统                       ''\n'
          '*****************************************************************''\n'
          '     1.生成6位数字防伪编码 （213563型）                          ''\n'
          '     2.生成9位系列产品数字防伪编码 （879-335439型）              ''\n'
          '     3.生成25位混合产品序列号 （B2R12-N7TE8-9IET2-FE350-DW2K4型）''\n'
          '     4.生成含数据分析功能的防伪编码 （5A61M0583D2）              ''\n'
          '     5.智能批量生成带据分析功能的防伪码                          ''\n'
          '     6.后续补加生成防伪码 （5A61M0583D2）                        ''\n'
          '     7.EAN-13条形码批量生成                                      ''\n'
          '     8.二维码批量输出                                            ''\n'
          '     0.退出系统                                                  ''\n'
          '=================================================================''\n'
          '说明：通过数字键选择菜单                                         ''\n'
          '================================================================='
          '\033[0m')


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print('\033[1;31;40m  输入非法，请重新输入！ \033[0m')
            return 0
        else:
            return insel
    else:
        print('\033[1;31;40m  输入4非法，请重新输入！\033[0m')
        return 0


def scode1(schoice):
    incount = inputbox('\033[1;32m  请输入您要生成的防伪码数量：\033[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m  请输入您要生成的防伪码数量：\033[0m', 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ''
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + '\n'
        randstr.append(randfir)
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成6位防伪码共计：', 'codepath')


def scode2(schoice):
    print(13456)
    ordstart = inputbox('\033[1;32m 请输入产品的数字起始号（3位）：\33[0m', 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox('\033[1;32m 请输入产品的数字起始号（3位）：\33[0m', 1, 0)
    ordcount = inputbox('\033[1;32m 请输入产品系列的数量', 1, 0)
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox('\033[1;32m 请输入产品系列的数量', 1, 0)
    incount = inputbox('\033[1;32m 请输入要生成的每个系列产品的防伪码数量：\33[0m', 1, 0)
    while int(ordstart) == 0:
        incount = inputbox('\033[1;32m 请输入要生成的每个系列产品的防伪码数量：\33[0m', 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + '\n')
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成9位系列产品防伪码共计：', 'codepath')


def scode3(schoice):
    incount = inputbox('\033[1;32m  请输入要生成的25位混合产品序列号数量：\33[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m  请输入要生成的25位混合产品序列号数量：\33[0m', 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ''
        for i in range(25):
            strone = strone + random.choice(letter)
        strtwo = strone[:5] + '-' + strone[5:10] + '-' + strone[10:15] + '-' + strone[15:20] + '-' + strone[
                                                                                                     20:25] + '\n'
        randstr.append(strtwo)
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成25混合防伪序列码共计：', 'codepath')


def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    for j in range(int(scount)):
        strpro = typestr[0].upper()
        strtype = typestr[1].upper()
        strclass = typestr[2].upper()
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        letterone = ''
        for i in range(9):
            letterone = letterone + random.choice(number)
        sim = str(letterone[0:int(randsec[0])]) + strpro + str(
            letterone[int(randsec[0]):int(randsec[1])]) + strpro + str(
            letterone[int(randsec[1]):int(randsec[2])]) + strpro + str(letterone[int(randsec[2]):9]) + '\n'
        randstr.append(sim)
        wfile(randstr, typestr + 'scode' + str(schoice) + '.txt', ismessage, '生成含数据分析功能的防伪码共计：', 'codepath')


def scode4(schoice):
    intype = inputbox('\033[1;32m 请输入数据分析编号（3位字母）：\33[0m', 2, 3)
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox('\033[1;32m 请输入数据分析编号（3位字母）：\33[0m', 2, 3)
    incount = inputbox('\033[1;32m 输入要生成的带数据分析功能的防伪码数量：\33[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m 输入要生成的带数据分析功能的防伪码数量：\33[0m', 1, 0)
    ffcode(incount, intype, '', schoice)


def scode5(schoice):
    default_dir = r'codeauto.mri'
    file_path = tkinter.filedialog.askopenfilename(filetypes=[('Text file', '*.mri')], title=u'请选择智能批处理文件：',
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split('\n')
    print(codelist)
    for item in codelist:
        codea = item.split(',')[0]
        codeb = item.split(',')[1]
        ffcode(codeb, codea, 'no', schoice)


def scode6(schoice):
    default_dir = r'd:\ABDscode5.txt'
    file_path = tkinter.filedialog.askopenfilename(title=u'请选择已经生成的防伪码文件', initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split('\n')
    codelist.remove('')
    strset = codelist[0]
    remove_digits = strset.maketrans('', '', digits)
    res_letter = strset.translate(remove_digits)
    nres_letter = list(res_letter)
    strpro = nres_letter[0]
    strtype = nres_letter[1]
    strclass = nres_letter[2]
    nres_letter = strpro.replace(''''','').replace(''''', '') + strtype.replace(
        ''''','').replace(''''', '') + strclass.replace(''''','').replace(''''', '')
    card = set(codelist)
    tkinter.messagebox.showinfo('提示', '之前的防伪码共计：' + str(len(card)))
    root.withdraw()
    incount = inputbox('请输入补充防伪码生成的数量：', 1, 0)
    for j in range(int(incount) * 2):
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        addcount = len(card)
        strone = ''
        for i in range(9):
            strone = strone + random.choice(number)
        sim = str(strone[0:int(randsec[0])]) + strpro + str(
            strone[int(randsec[0]):int(randsec[1])]) + strpro + str(
            strone[int(randsec[1]):int(randsec[2])]) + strpro + str(strone[int(randsec[2]):9]) + '\n'
        card.add(sim)
        if len(card) > addcount:
            randstr.append(sim)
            addcount = len(card)
        if len(randstr) >= int(incount):
            print(len(randstr))
            break
    wfile(randstr, nres_letter + 'ncode' + str(choice) + '.txt', nres_letter, '生成后补防伪码共计：', 'codeadd')


def scode7(schoice):
    mainid = inputbox('\033[1;32m  请输入EN13的国家代码（3位）：\033[0m', 1, 0)
    while int(mainid) < 1 or len(mainid) != 3:
        mainid = inputbox('\033[1;32m  请输入EN13的国家代码（3位）：\033[0m', 1, 0)
    compid = inputbox('\033[1;32m  请输入企业代码（4位）：\033[0m', 1, 0)
    while int(compid) < 1 or len(compid) != 4:
        compid = inputbox('\033[1;32m  请输入EN13的企业代码（4位）：\033[0m', 1, 0)
    incount = inputbox('\033[1;32m  请输入要生成的条形码数量：\033[0m', 1, 0)
    while incount == 0:
        incount = inputbox('\033[1;32m  请输入要生成的条形码数量：\033[0m', 1, 0)
    mkdir('barcode')
    for j in range(int(incount)):
        strone = ''
        for i in range(5):
            strone = strone + str(random.choice(number))
        barcode = mainid + compid + strone
        evensum = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + int(
            barcode[11])
        oddsum = int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(barcode[10])
        checkbit = int(10 - ((evensum * 3 + oddsum) % 10) % 10)
        barcode = barcode + str(checkbit)
        encoder = EAN13Encoder(barcode)
        encoder.save('barcode\\' + barcode + '.png')


def scode8(schoice):
    incount = inputbox('\033[1;32m  请输入要生成的12位数字二维码数量:\33[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m  请输入要生成的12位数字二维码数量:\33[0m', 1, 0)
    mkdir('qrcode')
    for j in range(int(incount)):
        strone = ''
        for i in range(12):
            strone = strone + str(random.choice(number))
        encoder = qrcode.make(strone)
        encoder.save('qrcode\\' + strone + '.png')
    print('\033[1;32m  已经保存到qrcode文件夹中！\033[0m')


while i < 9:
    mainmenu()
    choice = input('\033[1;32m  请您输入您要操作的菜单选项：\033[0m')
    if len(choice) != 0:
        choice = input_validation(choice)
        if choice == '1':
            scode1(choice)
        elif choice == '2':
            scode2(choice)
        elif choice == '3':
            scode3(choice)
        elif choice == '4':
            scode4(choice)
        elif choice == '5':
            scode5(choice)
        elif choice == '6':
            scode6(choice)
        elif choice == '7':
            scode7(choice)
        elif choice == '8':
            scode8(choice)
        elif choice == '0':
            i = 0
            print('已退出系统！')
            break
    else:
        print('\033[1;31;40m  输入5非法，请重新输入！\033[0m')
        time.sleep(2)
