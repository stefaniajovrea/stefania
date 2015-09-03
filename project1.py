import networkx as nx
import matplotlib.pyplot as plt
import dblp 

def get_right_name(list_of_auth, name):
	for i in list_of_auth:
		if i.name == name:
			print i.name
			return 0
	
def _main():
    g = nx.Graph()

    authors = dblp.search('Cosmin Bonchis')
    cosmin=authors[0]
    authors1 = dblp.search('Stefan Balint')
    stefanb=authors1[0]
    authors2 = dblp.search('Adrian Craciun')
    adrian=authors2[0]
    authors3 = dblp.search('Roxana Dogaru')
    roxana=authors3[0]
    authors4 = dblp.search('Teodor-Florin Fortis')
    teodor=authors4[0]
    authors5 = dblp.search('Marc Frincu')
    marc=authors5[0]
    authors6 = dblp.search('Victoria Iordan')
    victoria=authors6[0]
    authors7 = dblp.search('Gabriel Istrate')
    gabriel=authors7[0]
    authors8 = dblp.search('Ciprian Jichici')
    ciprianj=authors8[0]
    authors9 = dblp.search('Gabriel Iuhasz')
    iuhasz=authors9[0]
    authors10 = dblp.search('Eva Kaslik')
    eva=authors10[0]
    authors11 = dblp.search('Mircea Marin')
    mircea=authors11[0]
    authors12 = dblp.search('Flavia Micota')
    flavia=authors12[0]
    authors13 = dblp.search('Cristina Mindruta')
    cristina=authors13[0]
    authors14 = dblp.search('Stefan Maruster')
    stefanm=authors14[0]
    authors15 = dblp.search('Marian Neagul')
    marian=authors15[0]
    authors16 = dblp.search('Viorel Negru')
    viorel=authors16[0]
    authors17 = dblp.search('Dana Petcu')
    dana=authors17[0]
    authors18 = dblp.search('Daniel Pop')
    get_right_name(authors18,'Daniel Pop')
    pop=authors18[0]
    authors19 = dblp.search('Horia Popa')
    horia=authors19[0]
    authors20 = dblp.search('Ciprian Pungila')
    ciprianp=authors20[0]
    authors21 = dblp.search('Monica Tirea')
    monica=authors21[0]
    authors22 = dblp.search('Daniela Zaharie')
    daniela=authors22[0]
    authors23 = dblp.search('Calin Sandru')
    calin=authors23[0]


    g.add_edge(stefanb.name, eva.name, weight=6 )
    g.add_edge(stefanb.name, teodor.name, weight=4 )
    g.add_edge(cosmin.name, gabriel.name, weight=6)
    g.add_edge(cosmin.name, dana.name, weight=1)
 
    g.add_edge(adrian.name, gabriel.name, weight=4)
    g.add_edge(adrian.name, mircea.name, weight=2)
    g.add_edge(roxana.name, flavia.name, weight=1)
    g.add_edge(roxana.name, daniela.name, weight=1)
 
    g.add_edge(teodor.name, viorel.name, weight=14)
    g.add_edge(teodor.name, pop.name, weight=2)
    g.add_edge(teodor.name, cristina.name, weight=3)
    g.add_edge(marc.name, dana.name, weight=16)

    g.add_edge(marc.name, marian.name, weight=4)
    g.add_edge(marc.name, daniela.name, weight=3)
    g.add_edge(victoria.name, dana.name, weight=2)
    g.add_edge(gabriel.name, mircea.name, weight=3)

    g.add_edge(ciprianj.name, pop.name, weight=1)
    g.add_edge(ciprianj.name, viorel.name, weight=1)
    g.add_edge(iuhasz.name, dana.name, weight=1)
    g.add_edge(iuhasz.name,viorel.name, weight=6)
 
    g.add_edge(iuhasz.name,daniela.name, weight=1)
    g.add_edge(iuhasz.name, monica.name, weight=1)
    g.add_edge(eva.name, dana.name, weight=1)
    g.add_edge(flavia.name, daniela.name, weight=1)

    g.add_edge(cristina.name, viorel.name, weight=2)
    g.add_edge(cristina.name, calin.name, weight=2)
    g.add_edge(cristina.name, dana.name, weight=1)
    g.add_edge(stefanm.name, viorel.name, weight=1)

    g.add_edge(marian.name, dana.name, weight=11)
    g.add_edge(marian.name, calin.name, weight=2)
    g.add_edge(marian.name, daniela.name, weight=2)
    g.add_edge(marian.name, pop.name, weight=1)

    g.add_edge(viorel.name, ciprianp.name, weight=5)
    g.add_edge(viorel.name, daniela.name, weight=17)
    g.add_edge(viorel.name, calin.name, weight=6)
    g.add_edge(viorel.name, pop.name, weight=9)

    g.add_edge(viorel.name, monica.name, weight=9)
    g.add_edge(viorel.name, dana.name, weight=10)
    g.add_edge(viorel.name, horia.name, weight=8)
    g.add_edge(dana.name, calin.name, weight=4)

    g.add_edge(dana.name, daniela.name, weight=15)
    g.add_edge(dana.name, pop.name, weight=1)
    g.add_edge(dana.name, horia.name, weight=1)

    g.add_edge(pop.name, daniela.name, weight=1)
    g.add_edge(pop.name, calin.name, weight=2)
    g.add_edge(pop.name, horia.name, weight=2)
    g.add_edge(horia.name, daniela.name, weight=1)

   

    pos = nx.circular_layout(g)
 
    edge_labels = { (u,v): d['weight'] for u,v,d in g.edges(data=True) }
 
    nx.draw_networkx_nodes(g,pos,node_size=1600,node_color= 'white',
               node_alpha=0.2,
               node_text_size=6,
               edge_color='blue', edge_alpha=0.2, edge_tickness=1,
               edge_text_pos=0.2,
               text_font='sans-serif')

    nx.draw_networkx_edges(g,pos)
    nx.draw_networkx_labels(g,pos)
    nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)
 
    plt.title("Professors Graph")
    plt.axis('off')
 
    plt.savefig('output.png')
    plt.show()
 
if __name__ == '__main__':
    _main()
