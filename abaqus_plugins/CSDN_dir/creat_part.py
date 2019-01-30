
from abaqus import * 
from abaqusConstants import *


def creat_part(name,length, width, height):

    # -*- coding: mbcs -*-
    #
    # Abaqus/CAE Release 6.14-4 replay file
    # Internal Version: 2015_06_12-04.41.13 135079
    # Run by yanguowei on Wed Jan 30 12:54:57 2019
    #

    # from driverUtils import executeOnCaeGraphicsStartup
    # executeOnCaeGraphicsStartup()
    #: Executing "onCaeGraphicsStartup()" in the site directory ...

    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=207.385406494141,
                     height=31.0)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()
    from caeModules import *
    from driverUtils import executeOnCaeStartup
    executeOnCaeStartup()
    Mdb()
    #: A new model database has been created.
    #: The model "Model-1" has been created.
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=168.36,
                                                    farPlane=208.764, width=139.755, height=65.8,
                                                    cameraPosition=(-5.77065,
                                                                    3.49905, 188.562),
                                                    cameraTarget=(-5.77065, 3.49905, 0))
    s.rectangle(point1=(0.0, 0.0), point2=(length, width))
    p = mdb.models['Model-1'].Part(name=name, dimensionality=THREE_D,
                                   type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts[name]
    p.BaseSolidExtrude(sketch=s, depth=height)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[name]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
