import traceback
import config

from model import *
from retrieval import retrieve_translation_pieces
from tqdm import tqdm

def decode_python_dataset(model, dataset, dataset_type="test_data", retrieval=False, verbose=True):
    # dataset = eval(dataset_type)
    from lang.py.parse import decode_tree_to_python_ast
    if verbose:
        logging.info('decoding [%s] set, num. examples: %d', dataset.name, dataset.count)

    decode_results = []
    cum_num = 0
    #raw_ids_to_be_evaluated = [17586, 17862, 17965, 18373, 17041, 17166, 17704, 18549, 18715]
    raw_ids_to_be_evaluated = [17041]
    #for example in dataset.examples:
    for example in tqdm(dataset.examples, total=len(dataset.examples)):
        #if example.raw_id in raw_ids_to_be_evaluated:
        if True:
            print 'raw_id: %d' % example.raw_id
            if retrieval:
                ngrams = retrieve_translation_pieces(train_data, example)
                cand_list = model.decode_with_retrieval(example, dataset.grammar, dataset.terminal_vocab, ngrams,
                                                    beam_size=config.beam_size, max_time_step=config.decode_max_time_step, log=True)
            else:
                cand_list = model.decode(example, dataset.grammar, dataset.terminal_vocab,
                                     beam_size=config.beam_size, max_time_step=config.decode_max_time_step)


            exg_decode_results = []
            for cid, cand in enumerate(cand_list[:10]):
                try:
                    ast_tree = decode_tree_to_python_ast(cand.tree)
                    code = astor.to_source(ast_tree)
                    exg_decode_results.append((cid, cand, ast_tree, code))
                except:
                    if verbose:
                        print "Exception in converting tree to code:"
                        print '-' * 60
                        print 'raw_id: %d, beam pos: %d' % (example.raw_id, cid)
                        traceback.print_exc(file=sys.stdout)
                        print '-' * 60

            cum_num += 1
            if cum_num % 50 == 0 and verbose:
                print '%d examples so far ...' % cum_num

            decode_results.append(exg_decode_results)

    return decode_results

    # serialize_to_file(decode_results, '%s.decode_results.profile' % dataset.name)


def decode_ifttt_dataset(model, dataset, verbose=True):
    if verbose:
        logging.info('decoding [%s] set, num. examples: %d', dataset.name, dataset.count)

    decode_results = []
    cum_num = 0
    for example in dataset.examples:
        cand_list = model.decode(example, dataset.grammar, dataset.terminal_vocab,
                                 beam_size=config.beam_size, max_time_step=config.decode_max_time_step)

        exg_decode_results = []
        for cid, cand in enumerate(cand_list[:10]):
            try:
                exg_decode_results.append((cid, cand))
            except:
                if verbose:
                    print "Exception in converting tree to code:"
                    print '-' * 60
                    print 'raw_id: %d, beam pos: %d' % (example.raw_id, cid)
                    traceback.print_exc(file=sys.stdout)
                    print '-' * 60

        cum_num += 1
        if cum_num % 50 == 0 and verbose:
            print '%d examples so far ...' % cum_num

        decode_results.append(exg_decode_results)

    return decode_results
