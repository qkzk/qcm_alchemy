"""
title: db schema from database
author: carlos aguni
date: 2022/05/13

Creates a database schema from your tables
[source](https://crashlaker.github.io/database/2020/05/13/database_diagram_with_python_sqlalchemy.html)
"""


from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

# create the pydot graph object by autoloading all tables via a bound metadata object
graph = create_schema_graph(
    metadata=MetaData("postgresql://quentin:bla@localhost/qcm"),
    show_datatypes=False,  # The image would get nasty big if we'd show the datatypes
    show_indexes=False,  # ditto for indexes
    rankdir="LR",  # From left to right (instead of top to bottom)
    concentrate=False,  # Don't try to join the relation lines together
)
graph.write_png("dbschema.png")  # write out the file
