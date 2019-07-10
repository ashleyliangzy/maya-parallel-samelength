import pymel.core as pm
import pymel.util as pmu
import pymel.core.datatypes as dt

window=pm.window(title="align edge length",widthHeight=(350,350))
pm.columnLayout(rowSpacing=10)

startVertsList=[]
edgesList=[]
directionList = []
standardEdgeLen=0

#def OnChoosePlane(*args):
#    selectObjList=pm.ls(selection=True)
#    selectObj=selectObjList[0]
#    return selectObj

#pm.button(label='choose a plane',command=OnChoosePlane)
pm.text(label='1 choose some vertices as start')
def OnChooseStartVert(*args):
    global startVertsList
    startVertsList=pm.ls(selection=True,flatten=True)      
pm.button(label='choose start vertex',command=OnChooseStartVert)


pm.text(label='2 choose some edges')
def OnChooseEdge(*args):
    global edgesList
    edgesList=pm.ls(selection=True,flatten=True)
    print edgesList   
pm.button(label='choose edges',command=OnChooseEdge)


pm.text(label='3 choose an edge as reference length')
def OnChooseStandardEdge(*args):
    standardEdge=pm.ls(selection=True,flatten=True)
    global standardEdgeLen
    for v in standardEdge:
         standardEdgeLen=v.getLength('world')
    print edgesList     
pm.button(label='choose standard edge',command=OnChooseStandardEdge)

pm.text(label='4 choose an edge as reference direction')
def OnChooseDirectionEdge(*args):
    global directionList
    directionList=pm.ls(selection=True,flatten=True)
    print directionList
    
       
pm.button(label='choose direction edge',command=OnChooseDirectionEdge)
           

pm.text(label='5 align edges')
def OnAlignEdge(*args):
    print startVertsList
    print edgesList
    print standardEdgeLen
    
    
    
    for e in edgesList:
        connectVerts=e.connectedVertices()
        vIndex_end=0
        i=0
        startV=startVertsList[0]
        endV=startVertsList[0]
        print 'edge:',e
        
        
        for v in connectVerts:
            if v in startVertsList:
                startV=v
                print 'start:',startV
            if v not in startVertsList:
                endV=v
                vIndex_end=i
                print 'endV:',endV
            i=i+1
            
        startV_pos=startV.getPosition('world')
        endV_pos=endV.getPosition('world')
            
        for ed in directionList:
            dirconnectVerts=ed.connectedVertices()
            dirvIndex_end=0
            a=0
            dirstartV=startVertsList[0]
            direndV=startVertsList[0]
                
            for vd in dirconnectVerts:
                if vd in startVertsList:
                    dirstartV=vd
                    print 'dirstart:',dirstartV
                if vd not in startVertsList:
                    direndV=vd
                    dirvIndex_end=a
                    print 'direndV:',direndV
                a=a+1
                
            
        dirstartV_pos=dirstartV.getPosition('world')
        direndV_pos=direndV.getPosition('world')

        orientation=direndV_pos-dirstartV_pos
        orientation=orientation.normal()
        endV_pos_change=orientation*standardEdgeLen+startV_pos
        e.setPoint(endV_pos_change,vIndex_end,'world')
               
pm.button(label='align edge',command=OnAlignEdge)

pm.showWindow(window)





