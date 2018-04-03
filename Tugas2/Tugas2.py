import mapnik
m = mapnik.Map(1920,1080)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff7')

r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[Propinsi]'), 'DejaVu Sans Bold',5,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True

r.symbols.append(point_sym)
s.rules.append(r)

m.append_style('Ryan1',s)
ds = mapnik.Shapefile(file="INDONESIA_PROP.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Ryan1')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('orange'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Ryan2',s)
ds = mapnik.Shapefile(file="INDONESIA_KEC.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Ryan2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Ryan3',s)
ds = mapnik.Shapefile(file="IND_PNT_polyline.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Ryan3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Ryan4',s)
ds = mapnik.Shapefile(file="IND_SNG_polyline.shp")
layer = mapnik.Layer('Indonesia')
layer.datasource = ds
layer.styles.append('Ryan4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Ryan5',s)
ds = mapnik.Shapefile(file="IND_KOT_point.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Ryan5')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

s = mapnik.Style()
r = mapnik.Rule()

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename = 'tugu.jpeg'
point_sym.widht = mapnik.Expression("20")
point_sym.height = mapnik.Expression("20")
point_sym.allow_overlap=True
r.symbols.append(point_sym)

text_sym = mapnik.TextSymbolizer(mapnik.Expression('[NAME]') , 'DejaVu Sans Bold' , 5 , mapnik.Color('black'))
text_sym.hallo_radius = 1
text_sym.allow_overlap = True
text_sym.avoid_edges = False
r.symbols.append(text_sym)

s.rules.append(r)
m.append_style('airport point' , s)

ds = mapnik.MemoryDatasource()
f = mapnik.Feature(mapnik.Context(), 1)
f ['NAME'] = 'asd asbdashbd ahsbdasbd'
f.add_geometries_from_wkt("POINT(-7.245808 112.737785)")
ds.add_feature(f)

player = mapnik.Layer('airport_layer')
player.datasource = ds

m.zoom_all()
mapnik.render_to_file(m,'indonesia.pdf','pdf')
print "rendered image to 'indonesia.pdf"