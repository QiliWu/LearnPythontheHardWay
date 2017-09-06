from nose.tools import *
from ex48 import lexicon, parser


lexi = lexicon.scan("fighter kill bear")
sen = parser.Sentence(lexi[0], lexi[1], lexi[2])


def test_class_Sentence():
    assert_equal(sen.subject, 'fighter')
    assert_equal(sen.verb, 'kill')
    assert_equal(sen.object, 'bear')


def test_peek():
    assert_equal(parser.peek(lexi), 'noun')
    assert_equal(parser.peek([]), None)


def test_match():
    words = lexicon.scan("the bear will eat you")
    assert_equal(parser.match(words, 'noun'), None)
    assert_equal(parser.match(words, 'noun'), ('noun', 'bear'))


def test_verb():
    words = lexicon.scan("the bear will eat you")
    ## assert_raises(ParserError, parser.parse_verb, words)
    # NameError: global name 'ParseError' is not defined
    assert_raises(parser.ParserError, parser.parse_verb, words)
    words.pop(0)  # pop bear
    assert_equal(parser.parse_verb(words), ('verb', 'eat'))


def test_object():
    words = lexicon.scan("will bear west next")
    assert_equal(parser.parse_object(words), ('noun', 'bear'))
    assert_equal(parser.parse_object(words), ('direction', 'west'))
    assert_raises(parser.ParserError, parser.parse_object, words)


def test_subject():
    words = lexicon.scan("kill the bear")
    senten = parser.parse_subject(words, ('noun', 'fighter'))
    assert_equal(senten.subject, 'fighter')
    assert_equal(senten.verb, 'kill')
    assert_equal(senten.object, 'bear')


def test_sentence():
    words = lexicon.scan("the fighter will kill the bear")
    senten = parser.parse_sentence(words)
    assert_equal(senten.subject, 'fighter')
    assert_equal(senten.verb, 'kill')
    assert_equal(senten.object, 'bear')

    # no subject test
    words = lexicon.scan("kill the bear")
    senten = parser.parse_sentence(words)
    assert_equal(senten.subject, 'player')
    assert_equal(senten.verb, 'kill')
    assert_equal(senten.object, 'bear')

    # error test
    words = lexicon.scan("777 eat bear")
    assert_raises(parser.ParserError, parser.parse_sentence, words)  