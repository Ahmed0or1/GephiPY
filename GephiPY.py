"""
Created on sun Sep 6 13:00:00 2020
@author: Ahmed Alghamdi
"""
import sys
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import re
current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
# reading data
df = pd.read_csv('Data.csv')

gexf =ET.Element('gexf')
gexf.attrib["xmlns"] = "http://www.gexf.net/1.3"
gexf.attrib["version"] = "1.3"
gexf.attrib["xmlns:viz"] = "http://www.gexf.net/1.3/viz"
gexf.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
gexf.attrib["xsi:schemaLocation"] = "http://www.gexf.net/1.3 http://www.gexf.net/1.3/gexf.xsd"
meta = ET.SubElement(gexf,'meta')
meta.attrib["lastmodifieddate"] =current_time
ET.SubElement(meta,'creator').text="Gephi 0.9"
ET.SubElement(meta,'description').text="@author: Ahmed Alghamdi"
graph = ET.SubElement(gexf,'graph')
graph.attrib["defaultedgetype"] = "directed"
graph.attrib["timeformat"] = "datetime"
graph.attrib["timerepresentation"] = "timestamp"
graph.attrib["mode"] = "dynamic"
attributes = ET.SubElement(graph,'attributes')
attributes.attrib["class"] = "node"
attributes.attrib["mode"] = "static"
attribute = ET.SubElement(attributes,'attribute',id='twitter_type',title='twitter_type',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='lat',title='lat',type='double').text=" "
attribute = ET.SubElement(attributes,'attribute',id='lng',title='lng',type='double').text=" "
attribute = ET.SubElement(attributes,'attribute',id='place_country',title='place_country',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='place_type',title='place_type',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='place_fullname',title='place_fullname',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='place_name',title='place_name',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='created_at',title='created_at',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='lang',title='lang',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='possibly_sensitive',title='possibly_sensitive',type='boolean').text=" "
attribute = ET.SubElement(attributes,'attribute',id='quoted_status_permalink',title='quoted_status_permalink',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='description',title='description',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='email',title='email',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='profile_image',title='profile_image',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='friends_count',title='friends_count',type='integer').text=" "
attribute = ET.SubElement(attributes,'attribute',id='followers_count',title='followers_count',type='integer').text=" "
attribute = ET.SubElement(attributes,'attribute',id='real_name',title='real_name',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='location',title='location',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='emoji_alias',title='emoji_alias',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='emoji_html_decimal',title='emoji_html_decimal',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='emoji_utf8',title='emoji_utf8',type='string').text=" "
attribute = ET.SubElement(attributes,'attribute',id='Name',title='Name',type='string').text=" "
nodes = ET.SubElement(graph,'nodes')
# for loop-> node [ Tweets ]--------------------------------------------------------------
counter_nodes = 0
for i in range(len(df)):
    counter_nodes = counter_nodes +1
    print('Tweet by: '+df.Username[i])
    node =ET.SubElement(nodes,'node')
    node.attrib["id"] = str(df.Tweets[i])
    node.attrib["label"] = df.Tweets[i]
    spells = ET.SubElement(node,'spells')
    Date_Gephi = str(df.Date[i])
    Date_Gephi=Date_Gephi.replace(" ","T")
    spell = ET.SubElement(spells, 'spell', {'for': 'twitter_type', 'timestamp':Date_Gephi})
    attvalues = ET.SubElement(node,'attvalues')
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'twitter_type', 'value':'Tweet'})
    createdAt = str(df.Created[i])
    createdAt=createdAt.replace(" ","T")
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'created_at', 'value':createdAt})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'description', 'value':str(df.Name[i])})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'Retweets', 'value':str(df.Retweets[i])})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'friends_count', 'value':''})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'followers_count', 'value':''})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'real_name', 'value':''})

    viz_size = ET.SubElement(node,'viz:size',value='0').text=" "
    viz_position = ET.SubElement(node,'viz:position', x="0",y='0').text=" "
    viz_color = ET.SubElement(node,'viz:color',r="0",g="0",b="255").text=" "
    print('%s- find node [ Tweet ] %s ' % (counter_nodes, df.Username[i]))
    # end Node [ tweet ]--------------------------------------------------------------
# for loop-> node [ User ]--------------------------------------------------------
    counter_nodes = counter_nodes + 1
    node = ET.SubElement(nodes,'node')
    node.attrib["id"] = '@'+df.Username[i]
    node.attrib["label"] = '@'+df.Username[i]
    spells = ET.SubElement(node,'spells')
    spell = ET.SubElement(spells, 'spell', {'for': 'twitter_type', 'timestamp':Date_Gephi})
    attvalues = ET.SubElement(node,'attvalues')
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'twitter_type', 'value': 'User'})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'created_at', 'value': createdAt})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'description', 'value': str(df.Location[i])})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'profile_image', 'value': ''})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'friends_count', 'value': str(df.Followers[i])})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'followers_count', 'value':str(df.Followers[i])})
    attvalue = ET.SubElement(attvalues, 'attvalue', {'for': 'real_name', 'value':df.Name[i]})

    viz_size = ET.SubElement(node,'viz:size',value='0').text=""
    viz_position = ET.SubElement(node,'viz:position', x="0",y='0').text=""
    viz_color = ET.SubElement(node,'viz:color',r="255",g="0",b="0").text=""
    print('%s- find node [ User ] %s ' % (counter_nodes, df.Username[i]))
# end Node [ User ]--------------------------------------------------------------
# for loop-> edges -------> (  Tweets | Has_mention | Retweets | Retweets_from )
edges = ET.SubElement(graph,'edges')
counter_edges = 0
for i in range(len(df)):
    counter_edges = counter_edges +1
# -----------> 1-1 Tweets
    if (df.Retweeted[i] == False):
        edge = ET.SubElement(edges,'edge')
        edge.attrib["id"] =str(counter_edges)
        edge.attrib["source"] =str(df.Username[i])
        edge.attrib["target"] =str(df.Tweets[i])
        edge.attrib["Type"] = 'Directed'
        edge.attrib["kind"] = "Tweets"
        edge.attrib["weight"] = str(df.Retweets[i])
        Date_Gephi = str(df.Date[i])
        Date_Gephi = Date_Gephi.replace(" ", "T")
        edge.attrib["timestamp"] =Date_Gephi
        viz_color = ET.SubElement(edge,'viz:color',r="0",g="255",b="0").text=" "
        print('%s- find edge [ Tweet ] with: %s ' %(counter_nodes,df.Username[i]))
# -----------> 1-2 Has_mention
        Has_mention_array=re.findall(r"[@]\w+",df.Tweets[i])
        for j in range(len(Has_mention_array)):
            Has_mention_array[j] = Has_mention_array[j].replace('@', '')
            counter_edges = counter_edges + 1
            edge = ET.SubElement(edges, 'edge')
            edge.attrib["id"] = str(counter_edges)
            edge.attrib["source"] = str(df.Tweets[i])
            edge.attrib["target"] = str(Has_mention_array[j])
            edge.attrib["Type"] = "Directed"
            edge.attrib["kind"] = "Has_mention"
            edge.attrib["weight"] = str(df.Retweets[i])
            edge.attrib["timestamp"] =Date_Gephi
            viz2_color = ET.SubElement(edge, 'viz:color', r="255", g="0", b="0").text = " "
            print('%s- find edge [ Has_mention ] %s -> %s' %(counter_edges,df.Username[i],Has_mention_array[j]))
# -----------> 2-1 Retweets_from
    else:#if(df.Retweeted[i] == True):
        counter_edges = counter_edges + 1
        tweet_writer=re.findall(r"[@]\w+",df.Tweets[i])
        tweet_writer[0] = str(tweet_writer[0]).replace('@', '')
        edge = ET.SubElement(edges, 'edge')
        edge.attrib["id"] =str(counter_edges)
        edge.attrib["source"] = str(df.Username[i])
        edge.attrib["target"] =str(tweet_writer[0])
        edge.attrib["Type"] = 'Directed'
        edge.attrib["kind"] = "Retweets_from"
        edge.attrib["weight"] = str(df.Retweets[i])
        edge.attrib["timestamp"] =str(Date_Gephi)
        viz_color = ET.SubElement(edge, 'viz:color', r="255", g="0", b="255").text = " "
        print('%s- find edge [ Retweets_from ] %s -> %s ' %(counter_edges,df.Username[i],tweet_writer[0]))
# -----------> 2-2  Retweets
        counter_edges = counter_edges + 1
        edge = ET.SubElement(edges,'edge')
        edge.attrib["id"] =str(counter_edges)
        edge.attrib["source"] = str(df.Username[i])
        edge.attrib["target"] = str(df.Tweets[i])
        edge.attrib["Type"] = 'Directed'
        edge.attrib["kind"] = "Retweets"
        edge.attrib["weight"] = str(df.Retweets[i])
        edge.attrib["timestamp"] = str(Date_Gephi)
        viz_color = ET.SubElement(edge,'viz:color',r="0",g="0",b="255").text=" "
        print('%s- find edge [ Retweet ]  %s  -> %s ' %(counter_edges,df.Username[i],str(df.Tweets[i])))
# end edges ----------------------------------------------------------------------
def prettify(element, indent='  '):
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level+1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level-1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings
prettify(gexf)
tree = ET.ElementTree(gexf)
tree.write('GephiPY.gexf',encoding='UTF-8',xml_declaration=True)
print('Nodes: '+str(counter_nodes))
print('edges: '+str(counter_edges))
print('Here is your gephi project : ',sys.path[0])
