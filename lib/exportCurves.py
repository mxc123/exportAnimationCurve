# -*- encoding: utf-8 -*-
import sys
import os
import maya.cmds as cmds
def exportAnmiCurve(exportPath):#导出动画曲线 exportPath参数为导出的路径
    cmds.file(exportPath,force=True,op="precision=17;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1 ",type="animExport",f=1,es=1)

def getObject():
    geoName = []
    geoList = cmds.ls(assemblies=1, v=1)
    return geoList


def RunExport(path, publishPath=''):
    
    cmds.file(path, o=1, f=1)
    cmds.loadPlugin("animImportExport")
    abcPath = os.path.dirname(path)
    name = os.path.basename(path).split(".")[0]
    geoList = getObject() 
    cmds.select(geoList)
    fileDirs = abcPath+"/%s" % name
    exportAnmiCurve("%s.anim"%fileDirs)

