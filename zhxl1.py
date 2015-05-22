digraph G  { 
    edge [fontname="Fangsong"]
	node [shape=box, fontname="Fangsong" size="20,20"]
	A  [label = "总    裁" color=Yellow, style=filled, fontcolor=Black, fontsize=22, shape=box]  // node A
	B  [label = "财务副总" color=Gold, style=filled, fontcolor=Black, fontsize=22,shape=box]     // node B 
	C  [label = "营销副总" color=Gold, style=filled, fontcolor=Black, fontsize=22,shape=box]     // node C
	D  [label = "设计副总" color=Gold, style=filled, fontcolor=Black, fontsize=22,shape=box]     // node D
	E  [label = "采购经理" color=Red, style=filled, fontcolor=Black, fontsize=22,shape=circle]   // node E
	F  [label = "设计经理" color=Red, style=filled, fontcolor=Black, fontsize=22,shape=circle]   // node F	
	G  [label = "加盟 商"  color=SkyBlue, style=filled, fontcolor=Red, fontsize=22,shape=egg]    // node G
	H  [label = "直营 店"  color=SkyBlue, style=filled, fontcolor=Red, fontsize=22,shape=egg]    // node H
	A->{B,C,D} [label = "管理" color=Green fontcolor=Red]  // edge A->{B,C,D}
	C->E [style= "dashed", color="forestgreen"]            // edge C->E
	D->F [style= "dashed", color="forestgreen"]            // edge D->F
	B->{G,H}  [label = "主管" color=Green fontcolor=Red]   // edge B->{G,H}
}
