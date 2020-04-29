from flask import request, make_response, render_template, jsonify
from app import app
import random
import os

availableTexts = [
    {'filename': 'ATaleOfTwoCities.txt', 'title': 'A Tale of Two Cities', 'author': 'Charles Dickens'},
    {'filename': 'AliceWonderland.txt', 'title': 'Alice\'s Adventures in Wonderland', 'author': 'Lewis Carroll'},
    {'filename': 'CivilDisobedience.txt', 'title': 'Walden, and On The Duty Of Civil Disobedience', 'author': 'Henry David Thoreau'},
    {'filename': 'DonQuixote.txt', 'title': 'The History of Don Quixote', 'author': 'Miguel de Cervantes Saavedra'},
    {'filename': 'LeavesOfGrass.txt', 'title': 'Leaves of Grass', 'author': 'Walt Whitman'},
    {'filename': 'LesMiserables.txt', 'title': 'Les Misérables', 'author': 'Victor Hugo'},
    {'filename': 'OnLiberty.txt', 'title': 'On Liberty', 'author': 'John Stuart Mill'},
    {'filename': 'TheBrothersKaramazov.txt', 'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoyevsky'},
    {'filename': 'TheJungleBook.txt', 'title': 'The Jungle Book', 'author': 'Rudyard Kipling'},
    {'filename': 'TheOdyssey.txt', 'title': 'The Odyssey', 'author': 'Homer'},
    {'filename': 'TheScarletLetter.txt', 'title': 'The Scarlet Letter', 'author': 'Nathaniel Hawthorne'},
    {'filename': 'TheWonderfulWizardofOz.txt', 'title': 'The Wonderful Wizard of Oz', 'author': 'L. Frank Baum'},
    {'filename': 'Ulysses.txt', 'title': 'Ulysses', 'author': 'James Joyce'},
    {'filename': 'WarAndPeace.txt', 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
    {'filename': 'WorksOfEdgarAllanPoe.txt', 'title': 'The Works of Edgar Allan Poe', 'author': 'Edgar Allan Poe'},
]
startIdProp = 0.25
endIdProp = 0.75
maxAnswerLength = 64

@app.route('/', methods=['GET'])
def index():

    fileId, wordId, word, hideLeft, hideRight = _startSearch()

    response =  make_response(render_template('index.html', wordId=wordId, word=word, fileId=fileId, hideLeft=hideLeft, hideRight=hideRight))
    return response


@app.route('/updateWord', methods=['GET', 'POST'])
def updateWord():
    word = request.json.get('word')
    wordId = int(word.get('wordId'))
    fileId = int(word.get('fileId'))
    wordId, word, hideLeft, hideRight = _getCurrentWord(wordId, fileId)
    return jsonify({'wordId': wordId, 'word': word, 'hideLeft': hideLeft, 'hideRight': hideRight}), 200

@app.route('/reveal', methods=['GET', 'POST'])
def revealAnswer():
    file = request.json.get('file')
    fileId = int(file.get('fileId'))
    answer = availableTexts[fileId]['title'].strip() + ' by ' + availableTexts[fileId]['author'].strip()
    lastCharId = max(min(maxAnswerLength, len(answer)), 0)
    answer = answer[0:lastCharId]
    if lastCharId < len(answer):
        answer += '...'
    return jsonify({'answer': answer}), 200


def _getCurrentWord(wordId, fileId):
    filename = availableTexts[fileId]['filename']
    filename = os.path.join('app/books', filename)

    hideLeft = False
    hideRight = False
    with open(filename, 'r', encoding='utf8') as f:
        txt = f.read().split()
        txt = [word for word in txt if word]
        txtLength = len(txt)
        word = txt[wordId]
        if wordId == txtLength - 1:
            hideRight = True
        if wordId <= 0:
            wordId = 0
            hideLeft = True
    return wordId, word, hideLeft, hideRight


def _startSearch():
    fileId = random.randint(0, len(availableTexts) - 1)
    filename = availableTexts[fileId]['filename']
    print(f'Selected \'{filename}\'')
    filename = os.path.join('app/books', filename)

    hideLeft = False
    hideRight = False
    with open(filename, 'r', encoding='utf8') as f:
        txt = f.read().split()
        txt = [word for word in txt if word]
        txtLength = len(txt)
        startBound = int(startIdProp * txtLength)
        endbound =  int(endIdProp * txtLength)
        wordId = random.randint(startBound, endbound)
        word = txt[wordId]
        if wordId == txtLength - 1:
            hideRight = True
        if wordId <= 0:
            wordId = 0
            hideLeft = True
    return fileId, wordId, word, hideLeft, hideRight
