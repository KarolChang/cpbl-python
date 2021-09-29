def listScoreboard(data):
  # return data[0]
  print(data[0]['InningSeq'])
  if(data[0]['InningSeq'] <= 9):
    innings = 9
  else:
    innings = data[0]['InningSeq']

  boardInfo = {
    '1': [''] * innings,
    '2': [''] * innings
  }
  boardInfo['1'] += [0, 0, 0]
  boardInfo['2'] += [0, 0, 0]
  
  for item in data:
    # R, H, E
    # print('len1', len(boardInfo[item['VisitingHomeType']]))
    # print('len1 -t', type(len(boardInfo[item['VisitingHomeType']])))
    # print('len2', len(boardInfo[item['VisitingHomeType']])-3)
    # print('len2 -t', type(len(boardInfo[item['VisitingHomeType']])-3))
    boardInfo[item['VisitingHomeType']][len(boardInfo[item['VisitingHomeType']])-3] += item['ScoreCnt']
    boardInfo[item['VisitingHomeType']][len(boardInfo[item['VisitingHomeType']])-2] += item['HittingCnt']
    boardInfo[item['VisitingHomeType']][len(boardInfo[item['VisitingHomeType']])-1] += item['ErrorCnt']

    # 如果最新一半局的分數是0 & '比賽中' 就先不要顯示
    # if(index == 0 & item.ScoreCnt == 0 & this.gameInfo.gameStatus == '比賽中'):
    #   return

    # Scores
    boardInfo[item['VisitingHomeType']][int(item['InningSeq']-1)] = item['ScoreCnt']
  
  return boardInfo

# 如果最後一局不用打，score 改成 X
# if(this.gameInfo.gameStatus == '比賽結束' && boardInfo['2'][boardInfo['2'].length-3] > boardInfo['1'][boardInfo['1'].length-3]) {
#   boardInfo['2'][boardInfo['2'].length-4] = 'X'

# this.boardInfo = boardInfo