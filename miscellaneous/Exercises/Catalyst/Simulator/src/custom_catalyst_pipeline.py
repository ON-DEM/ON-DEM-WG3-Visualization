# script-version: 2.0
# Catalyst state generated using paraview version 5.10.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1363, 908]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [5.464101615137755, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.1110194653004493
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1363, 908)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Partitioned Dataset Reader'
particlesvtpd = XMLPartitionedDatasetReader(registrationName='particles')
particlesvtpd.TimeArray = 'None'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=particlesvtpd)
cellDatatoPointData1.CellDataArraytoprocess = ['collisions']

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(registrationName='GaussianResampling1', Input=cellDatatoPointData1)
gaussianResampling1.ResampleField = ['POINTS', 'collisions']
gaussianResampling1.ResamplingGrid = [100, 100, 100]
gaussianResampling1.ExtenttoResample = [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=gaussianResampling1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.831373, 0.909804, 0.980392, 0.03741768016086593, 0.74902, 0.862745, 0.960784, 0.07483536032173187, 0.694118, 0.827451, 0.941176, 0.14967072064346373, 0.568627, 0.760784, 0.921569, 0.22450608096519556, 0.45098, 0.705882, 0.901961, 0.29934144128692747, 0.345098, 0.643137, 0.858824, 0.3741768016086593, 0.247059, 0.572549, 0.819608, 0.4490121619303911, 0.180392, 0.521569, 0.780392, 0.4789463060590839, 0.14902, 0.490196, 0.74902, 0.5388145943164694, 0.129412, 0.447059, 0.709804, 0.5986828825738549, 0.101961, 0.427451, 0.690196, 0.6286170267025476, 0.094118, 0.403922, 0.658824, 0.6585511708312404, 0.090196, 0.392157, 0.639216, 0.6884853149599331, 0.082353, 0.368627, 0.619608, 0.7184194590886258, 0.070588, 0.352941, 0.6, 0.7483536032173186, 0.066667, 0.329412, 0.568627, 0.7782877473460114, 0.07451, 0.313725, 0.541176, 0.8082218914747041, 0.086275, 0.305882, 0.509804, 0.8381560356033969, 0.094118, 0.286275, 0.478431, 0.8680901797320895, 0.101961, 0.278431, 0.45098, 0.8980243238607822, 0.109804, 0.266667, 0.411765, 0.927958467989475, 0.113725, 0.258824, 0.380392, 0.9578926121181678, 0.113725, 0.25098, 0.34902, 0.9878267562468606, 0.109804, 0.266667, 0.321569, 1.0177609003755534, 0.105882, 0.301961, 0.262745, 1.0476950445042459, 0.094118, 0.309804, 0.243137, 1.0776291886329388, 0.082353, 0.321569, 0.227451, 1.1075633327616314, 0.07451, 0.341176, 0.219608, 1.1374974768903243, 0.070588, 0.360784, 0.211765, 1.167431621019017, 0.066667, 0.380392, 0.215686, 1.1973657651477099, 0.062745, 0.4, 0.176471, 1.2722011254694416, 0.07451, 0.419608, 0.145098, 1.3470364857911734, 0.086275, 0.439216, 0.117647, 1.4218718461129052, 0.121569, 0.470588, 0.117647, 1.4967072064346372, 0.184314, 0.501961, 0.14902, 1.5715425667563692, 0.254902, 0.541176, 0.188235, 1.646377927078101, 0.32549, 0.580392, 0.231373, 1.7212132873998327, 0.403922, 0.619608, 0.278431, 1.7960486477215645, 0.501961, 0.670588, 0.333333, 1.885851080107643, 0.592157, 0.729412, 0.4, 1.9457193683650285, 0.741176, 0.788235, 0.490196, 2.005587656622414, 0.858824, 0.858824, 0.603922, 2.0953900890084918, 0.921569, 0.835294, 0.580392, 2.2450608096519558, 0.901961, 0.729412, 0.494118, 2.3947315302954197, 0.858824, 0.584314, 0.388235, 2.5444022509388833, 0.8, 0.439216, 0.321569, 2.694072971582347, 0.678431, 0.298039, 0.203922, 2.8437436922258104, 0.54902, 0.168627, 0.109804, 2.9185790525475426, 0.478431, 0.082353, 0.047059, 2.9934144128692743, 0.45098, 0.007843, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.25, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice1Display.LookupTable = splatterValuesLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'SplatterValues'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.2
slice1Display.SelectScaleArray = 'SplatterValues'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'SplatterValues'
slice1Display.GaussianRadius = 0.01
slice1Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'SplatterValues']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.9608807577356326, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.9608807577356326, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for splatterValuesLUT in view renderView1
splatterValuesLUTColorBar = GetScalarBar(splatterValuesLUT, renderView1)
splatterValuesLUTColorBar.Title = 'SplatterValues'
splatterValuesLUTColorBar.ComponentTitle = ''

# set color bar visibility
splatterValuesLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.9934144128692743, 1.0, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
vTP1 = CreateExtractor('VTP', slice1, registrationName='VTP1')
# trace defaults for the extractor.
vTP1.Trigger = 'TimeStep'

# init the 'VTP' selected for 'Writer'
vTP1.Writer.FileName = 'Slice1_{timestep:06d}.pvtp'

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'TimeStep'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [1363, 908]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(vTP1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.ExtractsOutputDirectory = 'my_extracts'
options.GlobalTrigger = 'TimeStep'
options.EnableCatalystLive = 1
options.CatalystLiveTrigger = 'TimeStep'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
