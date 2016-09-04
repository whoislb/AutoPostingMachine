#!/usr/bin/python
#encoding:utf-8
__author__ = 'harbour'
import os
from PIL import Image
from numpy import *
import  operator

def img2vector(filename):
    returnvect=[]
    fr=open(filename)
    # print "转换向量中，请等待。。。。"
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnvect.append(int(lineStr[j]))
    return returnvect

def trainingdataset():
    hwlabel=[]
    trainingfilelist=os.listdir('trainingDigits')
    m=len(trainingfilelist)
    trainingmat=zeros((m,1024))
    for i in range(m):
        filenamestr=trainingfilelist[i]
        filestr=filenamestr.split('.')[0]
        classnumstr= filestr.split('_')[0]
        hwlabel.append(classnumstr)
        trainingmat[i,:]=img2vector('trainingDigits/%s' %filenamestr)
    # print "转换完毕！"
    return hwlabel,trainingmat

def classify(inputPoint,dataSet,labels,k):
  # print "开始分类。。。"
  dataSetSize = dataSet.shape[0]
  diffMat = tile(inputPoint,(dataSetSize,1))-dataSet
  sqDiffMat = diffMat ** 2
  sqDistances = sqDiffMat.sum(axis=1)
  distances = sqDistances ** 0.5
  sortedDistIndicies = distances.argsort()
  classCount = {}
  for i in range(k):
    voteIlabel = labels[ sortedDistIndicies[i] ]
    classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
  sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
  # print "分类结束！输出结果。。"
  return sortedClassCount[0][0]

def knn(file):
    testvector=img2vector(file)
    hwlabel,trainingmat=trainingdataset()
    classifierresult=classify(testvector,trainingmat,hwlabel,3)
    return classifierresult