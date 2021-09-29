def listScoreboard(data):
  if(data[0]['InningSeq'] <= 9):
    innings = 9
  else:
    innings = data[0]['InningSeq']

  boardInfo = {
    '1': [''] * innings,
    '2': [''] * innings,
    'lastInning': data[0]['InningSeq'],
    'lastInningHalf': data[0]['VisitingHomeType']
  }
  boardInfo['1'] += [0, 0, 0]
  boardInfo['2'] += [0, 0, 0]
  
  for item in data:
    # R, H, E
    boardInfo[item['VisitingHomeType']][len(boardInfo[item['VisitingHomeType']])-3] += item['ScoreCnt']
    boardInfo[item['VisitingHomeType']][len(boardInfo[item['VisitingHomeType']])-2] += item['HittingCnt']
    boardInfo[item['VisitingHomeType']][len(boardInfo[item['VisitingHomeType']])-1] += item['ErrorCnt']

    # Scores
    boardInfo[item['VisitingHomeType']][int(item['InningSeq']-1)] = item['ScoreCnt']
  
  return boardInfo