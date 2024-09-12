from __future__ import unicode_literals
import pandas as pd
from templates import *
from pyarabic.araby import strip_tashkeel
from IPython.display import display, HTML
#######################
v=pd.read_csv('corpus/PoemsTreebank.csv',sep='\t',encoding='utf-16')
pos=pd.read_csv('corpus/pos.csv',sep='\t',encoding='utf-16')
pos_ar={pos.pos.iloc[i]:pos.pos_ar.iloc[i] for i in range(len(pos))}
pos_en={pos.pos_ar.iloc[i]:pos.pos.iloc[i] for i in range(len(pos))}
ctags={pos.pos_ar.iloc[i]:pos.color.iloc[i] for i in range(len(pos))}
#######################
rel=pd.read_csv('corpus/RelLabels.csv',sep='\t',encoding='utf-16')
rel_ar={rel.rel_en.iloc[i]:rel.rel_ar.iloc[i] for i in range(len(rel))}
rel_en={rel.rel_ar.iloc[i]:rel.rel_en.iloc[i] for i in range(len(rel))}
crel={rel.rel_ar.iloc[i]:rel.rel_color.iloc[i] for i in range(len(rel))}
#######################
def get_color(dic, color):
    return dic.get(color, 'blue')

def group_phrase_elements(numbers,elements):
    grouped_elements = []
    for current_number in numbers:
        if current_number != 0:
            if not grouped_elements or current_number != grouped_elements[-1][0]:
                grouped_elements.append([current_number])
            else:
                grouped_elements[-1].append(current_number)
        else:
            grouped_elements.append([0])
    lengths=[len(i) for i in grouped_elements]
    result = [];  index = 0
    for length in lengths:
        result.append(elements[index:index + length])
        index += length
    phrase=' '.join([''.join(i) for i in result])
    return phrase

######################
def get_item_levels(q):
    levels=[{'node':[],'sens':[],'level':[-1 for i in range(len(q))]}]
    revers_id=list(range(len(q)))[::-1]
    for i in range(1,max(q.constituent_levels)+1):
        l1=[[int(j) for j in i[1:-1].split('-')] for i in q[q.constituent_levels==i].constituents_loc]
        l2=[i for i in q[(q.constituent_levels==i)].constituent]
        l1= [[j for j in range(i[0],i[1]+1)] for i in l1]
        l=[-1 for i in range(len(q))]
        for c in range(len(l1)):
            for j in l1[c]:
                l[j]=c
        levels.append({'node':[[revers_id.index(j) for j in i][::-1] for i in l1][::-1],
                       'sens':[i for i in l2][::-1], 
                       'level':[revers_id.index(i) if i!=-1 else i for i in l][::-1]})
    return levels

def get_chapter_ayah(ayah):
    chapter={0:'لِمَغيبِ قَلْبي في هَواكُمْ مَشْهَدُ',
             1:'لَيْسَ الوُقوفُ بِكُفْءِ شَوْقِكَ فَاِنْزِلِ'}
    vers=sorted(list(set(ayah.verse_id)))
    sorh_ayah='[قصيدة '+ chapter[ayah.chapter_id.iloc[0]]+'. '
    if len(vers)==1:
        sorh_ayah=sorh_ayah+ 'البيت ' +str(vers[0])+']'
    else:
        sorh_ayah=sorh_ayah+ 'الابيات '+ str(vers)[1:-1]+']'
    return sorh_ayah


def get_text_arc(s1,f1,f2,level):
    texts=[];arcs=[]; node=[]; sens=[]
    for i in range(len(f1)):
        test=1
        if f1.depend_rel.iloc[i]==0 and f1.head_rel.iloc[i]==0: # token with token
            text=[[f1.uthmani_token.iloc[i],f1.pos.iloc[i],f1.token_id.iloc[i]],
                  [f2.uthmani_token.iloc[i],f2.pos.iloc[i],f2.token_id.iloc[i]]]
            arc= [f1.token_id.iloc[i],f1.ref_token_id.iloc[i],f1.rel_label.iloc[i],f1.rel_dir.iloc[i]]
        elif f1.depend_rel.iloc[i]==0 and f1.head_rel.iloc[i]==1: # token with node
            text=[[f1.uthmani_token.iloc[i],f1.pos.iloc[i],f1.token_id.iloc[i]],
                  [f2.constituent.iloc[i],f2.constituent_label.iloc[i],f2.constituents_locs.iloc[i]]]
            arc= [f1.token_id.iloc[i],f2.constituents_locs.iloc[i],f1.rel_label.iloc[i],f1.rel_dir.iloc[i]]
            node.append(f2.constituents_loc.iloc[i])
            sens.append(f2.constituent.iloc[i])
        elif f1.depend_rel.iloc[i]==1 and f1.head_rel.iloc[i]==0: # node with token
            text=[[f1.constituent.iloc[i],f1.constituent_label.iloc[i],f1.constituents_locs.iloc[i]],
                  [f2.uthmani_token.iloc[i],f2.pos.iloc[i],f2.token_id.iloc[i]]]
            arc= [f1.constituents_locs.iloc[i],f1.ref_token_id.iloc[i],f1.rel_label.iloc[i],f1.rel_dir.iloc[i]]
            node.append(f1.constituents_loc.iloc[i])
            sens.append(f1.constituent.iloc[i])
        elif f1.depend_rel.iloc[i]==1 and f1.head_rel.iloc[i]==1: # node with node
            text=[[f1.constituent.iloc[i],f1.constituent_label.iloc[i],f1.constituents_locs.iloc[i]],
                  [f2.constituent.iloc[i],f2.constituent_label.iloc[i],f2.constituents_locs.iloc[i]]]
            arc= [f1.constituents_locs.iloc[i],f2.constituents_locs.iloc[i],f1.rel_label.iloc[i],f1.rel_dir.iloc[i]]
            node.extend([f1.constituents_loc.iloc[i],f2.constituents_loc.iloc[i]])
            sens.extend([f1.constituent.iloc[i],f2.constituent.iloc[i]])
        else:
            test=0
            print('errer')
        if test==1:
            texts.extend(text)
            arcs.append(arc)
    if level==0:
        texts=[{'text':s1.uthmani_token.iloc[i],'tag':s1.pos.iloc[i],'tcolor':get_color(ctags,s1.pos.iloc[i])} 
               for i in range(len(s1))]
        item_levels={'node':[],'sens':[]}
    else:
        texts=[{'text':i[0],'tag':i[1],'tcolor':get_color(ctags,i[1]),'loc':i[2]} for i in texts]
        item_levels={'node':node,'sens':sens}
    arcs=[{'start':min(i[0],i[1]),'end':max(i[0],i[1]), 'label':i[2], 'dir':i[3],'acolor':get_color(crel,i[2])} for i in arcs]
    return texts,arcs,item_levels

def get_data_calculation(sid):
    s=v[v.sentence_id==sid].copy()
    sens=group_phrase_elements(list(s.sentence_word),list(s.uthmani_token))
    s['rel_dir'] = [ "_" if s.token_id.iloc[i] == s.ref_token_id.iloc[i] else
                          "right" if s.token_id.iloc[i] > s.ref_token_id.iloc[i] else "left" for i in range(len(s))]
    cl=[[] if i=='_' else [j for j in range(int(i[1:-1].split('-')[0]),int(i[1:-1].split('-')[-1])+1)] 
        for i in list(s.constituents_loc)]
    lev=[i for i in cl if i!=[]]
    main_list = sorted(lev, key=lambda x: len(x))
    ##################
    sub_list=[]; sub_levels=[]; test=0; n=0
    while main_list!=[] and test==0:
        m=[[i for j in main_list[0] if j in main_list[i]][0] for i in range(len(main_list)) 
           if [i for j in main_list[0] if j in main_list[i]] !=[]]
        sub_list.append([main_list[i] for i in m])
        for i in m[::-1]:
            del main_list[i]
        if main_list==[]:
            n+=1
            value=[i[0] for i in sub_list]
            #sub_levels.append({'level':n, 'value':value})
            sub_levels.append(value)
            main_list=sorted(sum([i[1:] for i in sub_list if len(i)>1],[]),key=lambda x: len(x))
            sub_list=[]
            if main_list==[]:
                test=1
    level=[0 if d==[] else int([[i+1 for j in sub_levels[i] if j==d] 
                                for i in range(len(sub_levels)) 
                                if [i+1 for j in sub_levels[i] if j==d]!=[]][0][0]) for d in cl]
    s.index=list(range(len(s)))
    s['constituent_levels']=level
    s['constituent']=['_' if d==[]
                      else group_phrase_elements(list(s[s.index.isin(d)].sentence_word),list(s[s.index.isin(d)].uthmani_token))
                      for d in cl]
    s['constituents_loc']=cl
    levels=[[i if j in sorted(list(s[s.constituent_levels==i].token_id)+list(s[s.constituent_levels==i].ref_token_id)
                              +list(s[s.ref_token_id.isin(list(s[(s.constituent_levels==i)].token_id))&
                                      (s.head_rel==1)&(s.constituent_levels==0)].token_id))
             else 0  for j in range(len(level))] for i in range(max(level)+1)]
    for l in range(1,len(levels)):
        t=[j for j in range(len(levels[l])) if levels[l][j]!=0]
        levels[l]=[0 if levels[l][i]==0 else 2 if (s.ref_token_id.iloc[i] in t and s.depend_rel.iloc[i] ==0 
                                                   and (s.constituent_levels[s.ref_token_id.iloc[i]]!=l)) 
                   else 1 if s.ref_token_id.iloc[i] in t and s.depend_rel.iloc[i] !=-1
                   else 2
                   for i in range(len(levels[l]))]
    s1=s[['token_id','uthmani_token','pos','ref_token_id' ,'rel_label','rel_dir','constituent','is_node',
       'constituent_levels','constituents_loc','constituent_label','depend_rel', 'head_rel']].copy()
    #level=get_item_levels(s)
    #s1['constituents_loc']=cl
    column_level=['level'+str(i) for i in range(len(levels))]
    for i in range(len(column_level)):
        s1[column_level[i]]=levels[i]
    s1['level0']=[1 if s1.depend_rel.iloc[i]==0 and s1.head_rel.iloc[i]==0 else 2 for i in range(len(s1))]
    s1['constituents_loc']=[[len(s)-j-1 for j in i][::-1] for i in s.constituents_loc]
    s1=s1[::-1]
    s1['token_id']=list(s1.token_id)[::-1]
    s1['ref_token_id']=[len(s1)-i-1 for i in list(s1.ref_token_id)]
    s1['constituents_locs']=[-1 if len(i)==0 else ((len(s1)-i[0]-1)+(len(s1)-i[-1]-1))/2 for i in cl[::-1]]
    ####################
    texts=[];arcs=[]; item_levels=[]
    for j in range(len(column_level)):
        f2=s1[:1]
        f1=s1[s1[column_level[j]]==1]
        for i in list(f1.ref_token_id):
            f2=pd.concat([f2,s1[s1.token_id==i]])
        f2=f2[1:]
        text,arc,item_level=get_text_arc(s1,f1,f2,j)
        texts.append(text)
        arcs.append(arc)
        item_levels.append(item_level)
    sorh_ayah=get_chapter_ayah(s)
    levs,len_words=len(arcs),len(texts[0])
    return levs,len_words,sens,sorh_ayah,texts,arcs,item_levels

##########################
def get_structure(sid,parse):
    levs,len_words,sens,sorh_ayah,text,arc,level=get_data_calculation(sid)
    parse=[DependencyRenderer().render_lev1_svg(i,i,len_words,text[i],arc[i]) for i in range(len(text))]
    height=200+sum([i['height'] for i in parse])
    h=0
    for i in range(len(parse)):
        h=h+ parse[i]['height']
        ty=height-(h-parse[i]['words'][0]['y'])
        for j in range(len(parse[i]['words'])):
            parse[i]['words'][j]['y']=ty
        for j in range(len(parse[i]['arcs'])):
            parse[i]['arcs'][j]['arc'][1]=height-(h-parse[i]['arcs'][j]['arc'][1])
            parse[i]['arcs'][j]['arc'][2]=height-(h-parse[i]['arcs'][j]['arc'][2])
            parse[i]['arcs'][j]['arrowhead'][2]=height-(h-parse[i]['arcs'][j]['arrowhead'][2])
            parse[i]['arcs'][j]['y_curve']=height-(h-parse[i]['arcs'][j]['y_curve'])
    return parse

#Each sentence's data is called to be processed independently
def get_constituent_structure(dep_parser,level):
    shift_x=1.5
    def sort_by_x(item):
        return item['x']
    word=[i['words'] for i in dep_parser]
    words=[word[0]]
    words.extend([sorted(word[i], key=sort_by_x) for i in range(1,len(word))])
    pt=[[i[j]['text'] for j in range(len(i))] for i in words]
    px=[[i[j]['x'] for j in range(len(i))] for i in words]
    py=[[i[j]['y'] for j in range(len(i))] for i in words]
    ls=[[j for j in i['sens']] for i in level]
    ln=[[j for j in i['node']] for i in level]
    #ll=[[j for j in i['level']] for i in level]
    pxs=[px[0]];pys=[py[0]];inds=[[]];pts=[[]]
    for i in range(1,len(px)):
        px1=[];py1=[]; ind=[]; pt1=[]
        for j in range(len(ls[i])):
            index=pt[i].index(ls[i][j])
            px1.append(px[i][index])
            py1.append(py[i][index])
            pt1.append(pt[i][index])
            pt[i][index]='wadee'
            ind.append(index)
        pxs.append(px1)
        pys.append(py1)
        inds.append(ind)
        pts.append(pt1)
    #####################
    pxx=[[i+shift_x for i in pxs[0]]]
    for x in range(1,len(pxs)):
        px1=[i for i in pxx[x-1]]
        for j in range(len(pxs[x])):
            for d in level[x]['node'][j]:
                px1[d]=pxs[x][j]
        pxx.append(px1)
    #############
    pyy=[pys[0]]
    for y in range(1,len(pys)):
        pyy.append([pys[y][0] for i in pys[0]])
    ###############
    constituent_parser=[[[pxx[i][j],pyy[i][j]] for j in range(len(pxx[i]))] for i in range(len(pxx))]
    constituent_parser=[[constituent_parser[i-1][j]+constituent_parser[i][j] for j in range(len(constituent_parser[i]))] 
                       for i in range(1,len(constituent_parser))]
    if len(constituent_parser)==0:
        constituent_parser=[[[int(px[0][i])+shift_x,py[0][i],int(px[0][i])+shift_x,py[0][i]] for i in range(len(px[0]))]]
    return constituent_parser


def minify_html(html):
    """Perform a template-specific, rudimentary HTML minification for displaCy.
    Disclaimer: NOT a general-purpose solution, only removes indentation and
    newlines.
    html (unicode): Markup to minify.
    RETURNS (unicode): "Minified" HTML.
    """
    return html
#.strip()
#.replace('    ', '').replace('\n', '')
    #return html.strip().replace('    ', '').replace('\n', '')

def escape_html(text):
    """Replace <, >, &, " with their HTML encoded representation. Intended to
    prevent HTML errors in rendered displaCy markup.
    text (unicode): The original text.
    RETURNS (unicode): Equivalent text to be safely used within HTML.
    """
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    return text



class DependencyRenderer(object):
    """Render dependency parses as SVGs."""
    style = 'dep'

    def __init__(self, options={}):
        """Initialise dependency renderer.
        options (dict): Visualiser-specific options (compact, word_spacing,
            arrow_spacing, arrow_width, arrow_stroke, distance, offset_x,
            color, bg, font)
        """
        self.compact = options.get('compact', False)
        self.word_spacing = options.get('word_spacing', 25) #30
        self.arrow_spacing = options.get('arrow_spacing',
                                         12 if self.compact else 20) # 20
        self.arrow_width = options.get('arrow_width',
                                       6 if self.compact else 4) #20
        self.arrow_stroke = options.get('arrow_stroke', 2)
        self.distance = options.get('distance', 150 if self.compact else 100)
        self.offset_x = options.get('offset_x', 50)
        self.color = options.get('color', '#000000')
        self.bg = options.get('bg', '#ffffff')
        self.font = options.get('font', 'hafs')    


    def render_lev1_svg(self, render_id, lev,lsen, words, arcs):
        #self.levels = self.get_levels(arcs)
        self.levels = sorted(list(set(map(lambda arc: arc['end'] - arc['start'], arcs))))
        self.highest_level = len(self.levels)
        self.offset_y = self.distance/2*self.highest_level+self.arrow_stroke
        #self.width = self.offset_x+lsen*self.distance
        self.width = len(words)*self.distance
        self.height = self.offset_y+4*self.word_spacing
        self.id = render_id
        if lev == 0:
            words = [self.render_word(w['text'], w['tag'], w['tcolor'], i) for i, w in enumerate(words)]
        else:
            words = [self.render_levs_word(w['text'], w['tag'], w['tcolor'], w['loc'], i) for i, w in enumerate(words)]
        arcs = [self.render_arrow(a['label'], a['start'], a['end'], a['dir'], a['acolor'], i) for i, a in enumerate(arcs)]
        return {'width':self.width, 'height': self.height, 'words':words, 'arcs':arcs}
        #'color':self.color, 'bg':self.bg, 'font':self.font,

    def render_word(self, text, tag,tcolor,i):
        y = self.offset_y+self.word_spacing
        x = self.offset_x+i*self.distance
        html_text = escape_html(text)
        tline='_'*int(len(strip_tashkeel('text'))*.6)
        return {'text':html_text, 'tag':tag, 'tcolor':tcolor, 'x':x, 'y':y ,'tline':tline}

    def render_levs_word(self, text, tag,tcolor,loc, i):
        y = self.offset_y+self.word_spacing
        x = self.offset_x+loc*self.distance
        html_text = escape_html(text)
        tline='_'*int(len(strip_tashkeel('text'))*.8)
        return {'text':html_text, 'tag':tag, 'tcolor':tcolor, 'x':x, 'y':y ,'tline':tline}
        #return [html_text, tag, tcolor, x, y,tline]
    
    def render_arrow(self, label, start, end, direction,acolor, i):
        level = self.levels.index(end-start)+1
        x_start = self.offset_x+start*self.distance #+self.arrow_spacing
        y = self.offset_y
        x_end = self.offset_x+end*self.distance
        y_curve = self.offset_y-level*self.distance/2
        x_curve = ((x_end - x_start)/2) + x_start - self.arrow_width
        if self.compact:
            y_curve = self.offset_y-level*self.distance/6
        if y_curve == 0 and len(self.levels) > 5:
            y_curve = -self.distance
        arc = [x_start, y, y_curve, x_end]
        y_curve=y_curve+((y-y_curve)/4)- self.word_spacing
        arrowhead = [direction, x_curve, y_curve]
        return {'id':self.id, 'arrowhead':arrowhead, 'label':label, 'arc':arc, 'acolor':acolor,
                'y_curve':y_curve, 'x_curve':x_curve}



class DependencyRenderer1(object):
    """Render dependency parses as SVGs."""
    style = 'dep'

    def __init__(self, options={}):
        """Initialise dependency renderer.
        options (dict): Visualiser-specific options (compact, word_spacing,
            arrow_spacing, arrow_width, arrow_stroke, distance, offset_x,
            color, bg, font)
        """
        self.compact = options.get('compact', False)
        self.word_spacing = options.get('word_spacing', 25) #30
        self.arrow_spacing = options.get('arrow_spacing',
                                         12 if self.compact else 20) # 20
        self.arrow_width = options.get('arrow_width',
                                       6 if self.compact else 4) #20
        self.arrow_stroke = options.get('arrow_stroke', 2)
        self.distance = options.get('distance', 150 if self.compact else 100)
        self.offset_x = options.get('offset_x', 50)
        self.color = options.get('color', '#000000')
        self.bg = options.get('bg', '#ffffff')
        self.font = options.get('font', 'hafs')

    def render_ayah_svg(self, render_id, sens, sorh_ayah, dep_parser,constituent_parser):
        """Render SVG.
        render_id (int): Unique ID, typically index of document.
        words (list): Individual words and their tags.
        arcs (list): Individual arcs and their start, end, direction and label.
        RETURNS (unicode): Rendered SVG markup.
        """
        width = dep_parser[0]['width']
        height = 200+sum([i['height'] for i in dep_parser])
        self.id = render_id        
        content=''
        constituents=''
        ############
        #cons=''
        y = 30
        x = width/2 # ,وضع الاية بالمنتصف
        html_text = escape_html(sens)
        ayah=TPL_DEP_AYAH.format(text='{'+sens+'}', tag=sorh_ayah, tcolor='DarkGreen', x=x, y=y, 
                                  tline='_'*int(len(strip_tashkeel(sorh_ayah))))
        con=['M'+' '.join([str(j) for j in [x,y+72]+i[-2:]]) for i in constituent_parser[-1]]
        for c in con:
            ayah = ''.join(ayah)+TPL_CON_PATH.format(constituent=c)
        ############
        constituent=[['M'+' '.join([str(h) for h in d]) for d in j] for j in constituent_parser]
        for c in constituent:
            for j in c:
                constituents = ''.join(constituents)+TPL_CON_PATH.format(constituent=j)
        ############
        for i in dep_parser:
            words=''; arcs='';n1=0;n2=0
            for j in i['words']:
                w=TPL_DEP_WORDS.format(text=j['text'], tag=j['tag'], tcolor=j['tcolor'], x=j['x'], y=j['y'],tline=j['tline'])
                words = ''.join(words) + ''.join(w)
            for j in i['arcs']:
                n2+=1
                arrowhead = self.get_arrowhead(j['arrowhead'][0], j['arrowhead'][1], j['arrowhead'][2])
                arc = self.get_arc(j['arc'][0], j['arc'][1], j['arc'][2], j['arc'][3])
                a=TPL_DEP_ARCS.format(id=render_id, i=n2, stroke=self.arrow_stroke, head=arrowhead, label=j['label'],
                                      arc=arc, acolor=j['acolor'],y_curve=j['y_curve'],x_curve=j['x_curve']+3)
                arcs = ''.join(arcs) + ''.join(a)
            content = ''.join(content) + ''.join(words) + ''.join(arcs)
        if len(constituent_parser)>0:
            content = ''.join(ayah) + ''.join(constituents) + ''.join(content)
        else:
            content = ''.join(ayah) + ''.join(content)
        return TPL_DEP_SVG.format(id=self.id, width=width, height=height, viewBox='0 0 ' +str(width)+' '+str(height),
                                  color=self.color, bg=self.bg, font=self.font, svg=content)


    def get_arc(self, x_start, y, y_curve, x_end):
        """Render individual arc.
        x_start (int): X-coordinate of arrow start point.
        y (int): Y-coordinate of arrow start and end point.
        y_curve (int): Y-corrdinate of Cubic Bézier y_curve point.
        x_end (int): X-coordinate of arrow end point.
        RETURNS (unicode): Definition of the arc path ('d' attribute).
        """
        template = "M{x},{y} C{x},{c} {e},{c} {e},{y}"
        if self.compact:
            template = "M{x},{y} {x},{c} {e},{c} {e},{y}"
        return template.format(x=x_start, y=y, c=y_curve, e=x_end)

    def get_arrowhead(self, direction, x, y):
        """Render individual arrow head.
        direction (unicode): Arrow direction, 'left' or 'right'.
        x (int): X-coordinate of arrow start point.
        y (int): Y-coordinate of arrow start and end point.
        end (int): X-coordinate of arrow end point.
        RETURNS (unicode): Definition of the arrow head path ('d' attribute).
        """
        if direction == 'left':
            pos = 'v-4 l-15 5 l15 5 v-4 z'
            arrowhead = (x+10, y + self.word_spacing-1,pos)
        else:
            pos = 'v-4 l15 5 l-15 5 v-4 z'
            arrowhead = (x, y + self.word_spacing-1,pos)
        return "M{},{} {} ".format(*arrowhead)
    
def get_visualization(sid):
    levs,len_words,sens,sorh_ayah,texts,arc,level=get_data_calculation(sid)
    parse1=[DependencyRenderer().render_lev1_svg(i,i,len_words,texts[i],arc[i]) for i in range(len(texts))]
    dep_parser=get_structure(sid,parse1)
    constituent_parser=get_constituent_structure(dep_parser,level)
    html = DependencyRenderer1()
    htm = html.render_ayah_svg(sid,sens,sorh_ayah, dep_parser,constituent_parser)
    return htm

style1="""<!DOCTYPE html>
<html lang="ar">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .container {
            width: 1654px;
            /* عرض الحاوية */
            margin: 0 auto;
            /* توسيط الحاوية */
        }

        .svg-container {
            width: 100%;
            /* لتحقيق تناسب الحاوية دون تمدد */
            display: flex;
            justify-content: center;
            margin-bottom: 50px;
        }

        .svg-container svg {
            /* جعل الصورة تمتلئ تمامًا داخل الحاوية */
            height: auto;
            justify-content: center;
        }
        
        .table-container {
          flex: 1;
          width: 90%;
          overflow: auto;
          /* إمكانية التمرير إذا كان الجدول كبيرًا */
          margin-bottom: 50px;
        }

        table {
          width: 100%;
          border-collapse: collapse;
        }

        th,
        td {
          border: 1px solid #ccc;
          padding: 8px;
          text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
    """
##dir="rtl"
style2="""                    <style>
                      .treebank {
                          direction: ltr;
                      }
                  
                      .treebank [font-family="hafs"] {
                          font-family: 'hafs-qc'
                      }
                  
                      .treebank [font-family="Times New Roman"] {
                          font-family: 'Kitab'
                      }
                  
                      @font-face {
                          font-family: 'hafs-qc';
                          src: url('https://fonts.nuqayah.com/hafs-qc.woff2');
                      }
                    .paragraph-style {
                      direction: rtl; /* اتجاه النص من اليمين إلى اليسار */
                      margin-top: 0in; /* هامش أعلى */
                      margin-right: 0in; /* هامش يمين */
                      margin-bottom: 0in; /* هامش أسفل */
                      margin-left: 0in; /* هامش يسار */
                      text-align: justify; /* محاذاة النص */
                      line-height: normal; /* ارتفاع السطر */
                    }
                    
                    .word-style-class {
                      color: black; /* Font color */
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                      font-size: 20px; /* Font size */
                      font-weight: bold; /* جعل الخط غامقًا */
                    }
                    
                    .td1-cell-style {
                      width: 150px; /* عرض الخلية */
                      border-top: none; /* إزالة الحدود العلوية */
                      border-right: none; /* إزالة الحدود اليمنى */
                      border-left: none; /* إزالة الحدود اليسرى */
                      border-image: initial; /* تعيين صورة الحدود */
                      border-bottom: 1pt solid rgb(127, 127, 127); /* حدود سفلية صلبة بلون رمادي */
                      padding: 0in 5.4pt; /* حشو الخلية */
                      vertical-align: top; /* محاذاة عمودية أعلى */
                    }
                    
                    .td2-cell-style {
                      width: 1500px; /* عرض الخلية */
                      border-top: none; /* إزالة الحدود العلوية */
                      border-right: none; /* إزالة الحدود اليمنى */
                      border-left: none; /* إزالة الحدود اليسرى */
                      border-image: initial; /* تعيين صورة الحدود */
                      border-bottom: 1pt solid rgb(127, 127, 127); /* حدود سفلية صلبة بلون رمادي */
                      padding: 0in 5.4pt; /* حشو الخلية */
                      vertical-align: top; /* محاذاة عمودية أعلى */
                    }
                    </style>
    </div>
</body>
</html>
"""

def visualization(sid):
    content=get_visualization(sid)
    html=''.join([style1,content,style2])
    display(HTML(html))

def visualization1(sid):
    content=get_visualization(sid)
    html=''.join([style1,content,style2])
    return html
##levs1,len_words1,sens1,sorh_ayah1,text1,arc1,level1=get_data_calculation(74)
