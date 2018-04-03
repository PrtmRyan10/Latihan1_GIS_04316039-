import mapnik
m = mapnik.Map(1600,800)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Blue') , 1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]') , 'DejaVu Sans Bold' ,5, mapnik.Color('black'))
basinsLabels.hallo_fill = mapnik.Color ('yellow')
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)


s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('red')
germany = mapnik.Rule()
germany.filter = mapnik.Expression("[NAME]='Germany'")
germany.symbols.append(highlight)
s.rules.append(germany)


m.append_style('Ryan', s)
ds = mapnik.Shapefile(file="ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Ryan')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'world.jpeg', 'jpeg')
print "rendered image to 'World.jpeg' "