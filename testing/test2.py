from lang_tagger import *
lid = LID()
lid = LID(model='lid_models/hinglish', etrans='nmt_models/eng2eng.pt', htrans='nmt_models/rom2hin.pt')
print lid.tag_sent(u'i thght mosam dfrnt hoga bs fog h'.split())
#[(u'i', u'en'), (u'thght', u'en'), (u'mosam', u'hi'), (u'dfrnt', u'en'), (u'hoga', u'hi'), (u'bs', u'hi'), (u'fog', u'en'), (u'h', u'hi')]
print lid.tag_sent(u'kafi dprsng situation hai yar'.split())
#[(u'kafi', u'hi'), (u'dprsng', u'en'), (u'situation', u'en'), (u'hai', u'hi'), (u'yar', u'hi')]
