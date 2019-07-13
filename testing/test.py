from three_step_decoding import *
tsd = ThreeStepDecoding('lid_models/hinglish', htrans='nmt_models/rom2hin.pt', etrans='nmt_models/eng2eng.pt')
print '\n'.join(['\t'.join(x) for x in tsd.tag_sent(u'i thght mosam dfrnt hoga bs fog h')])
