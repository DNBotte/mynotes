// query subset of the movie database:

MATCH (person:Person {name: 'Tom Hanks'})
MATCH path = (person)-[:ACTED_IN]->(m)<-[:DIRECTED]-(d)
RETURN path
