digraph G  { 
    edge [fontname="Fangsong"]
	node [shape=box, fontname="Fangsong" size="20,20"]
	A  [label = "��    ��" color=Yellow, style=filled, fontcolor=Black, fontsize=22, shape=box]  // node A
	B  [label = "������" color=Gold, style=filled, fontcolor=Black, fontsize=22,shape=box]     // node B 
	C  [label = "Ӫ������" color=Gold, style=filled, fontcolor=Black, fontsize=22,shape=box]     // node C
	D  [label = "��Ƹ���" color=Gold, style=filled, fontcolor=Black, fontsize=22,shape=box]     // node D
	E  [label = "�ɹ�����" color=Red, style=filled, fontcolor=Black, fontsize=22,shape=circle]   // node E
	F  [label = "��ƾ���" color=Red, style=filled, fontcolor=Black, fontsize=22,shape=circle]   // node F	
	G  [label = "���� ��"  color=SkyBlue, style=filled, fontcolor=Red, fontsize=22,shape=egg]    // node G
	H  [label = "ֱӪ ��"  color=SkyBlue, style=filled, fontcolor=Red, fontsize=22,shape=egg]    // node H
	A->{B,C,D} [label = "����" color=Green fontcolor=Red]  // edge A->{B,C,D}
	C->E [style= "dashed", color="forestgreen"]            // edge C->E
	D->F [style= "dashed", color="forestgreen"]            // edge D->F
	B->{G,H}  [label = "����" color=Green fontcolor=Red]   // edge B->{G,H}
}
