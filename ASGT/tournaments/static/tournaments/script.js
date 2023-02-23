
function GetPlayersScoreR1() {
  var score_r1_m1_p1 = document.getElementById("score-r1-m1-p1").value;
  var score_r1_m1_p2 = document.getElementById("score-r1-m1-p2").value;
  var score_r1_m2_p3 = document.getElementById("score-r1-m2-p3").value;
  var score_r1_m2_p4 = document.getElementById("score-r1-m2-p4").value;
  var score_r1_m3_p5 = document.getElementById("score-r1-m3-p5").value;
  var score_r1_m3_p6 = document.getElementById("score-r1-m3-p6").value;
  var score_r1_m4_p7 = document.getElementById("score-r1-m4-p7").value;
  var score_r1_m4_p8 = document.getElementById("score-r1-m4-p8").value;
  return[
    score_r1_m1_p1,
    score_r1_m1_p2,
    score_r1_m2_p3,
    score_r1_m2_p4,
    score_r1_m3_p5,
    score_r1_m3_p6,
    score_r1_m4_p7,
    score_r1_m4_p8
  ]
}

function GetPlayersScoreR2() {
  var score_r2_m1_p1 = document.getElementById("score-r2-m1-p1").value;
  var score_r2_m1_p2 = document.getElementById("score-r2-m1-p2").value;
  var score_r2_m2_p3 = document.getElementById("score-r2-m2-p3").value;
  var score_r2_m2_p4 = document.getElementById("score-r2-m2-p4").value;

  return[
    score_r2_m1_p1,
    score_r2_m1_p2,
    score_r2_m2_p3,
    score_r2_m2_p4,
  ]
}

function GetPlayerNameR1() {
  var player_r1_m1_p1 = document.getElementById("player-r1-m1-p1").textContent;
  var player_r1_m1_p2 = document.getElementById("player-r1-m1-p2").textContent;
  var player_r1_m2_p3 = document.getElementById("player-r1-m2-p3").textContent;
  var player_r1_m2_p4 = document.getElementById("player-r1-m2-p4").textContent;
  var player_r1_m3_p5 = document.getElementById("player-r1-m3-p5").textContent;
  var player_r1_m3_p6 = document.getElementById("player-r1-m3-p6").textContent;
  var player_r1_m4_p7 = document.getElementById("player-r1-m4-p7").textContent;
  var player_r1_m4_p8 = document.getElementById("player-r1-m4-p8").textContent;
  return[
    player_r1_m1_p1,
    player_r1_m1_p2,
    player_r1_m2_p3,
    player_r1_m2_p4,
    player_r1_m3_p5,
    player_r1_m3_p6,
    player_r1_m4_p7,
    player_r1_m4_p8
  ]
}

function GetPlayerNameR2() {
  var player_r2_m1_p1 = document.getElementById("player-r2-m1-p1").textContent;
  var player_r2_m1_p2 = document.getElementById("player-r2-m1-p2").textContent;
  var player_r2_m2_p3 = document.getElementById("player-r2-m2-p3").textContent;
  var player_r2_m2_p4 = document.getElementById("player-r2-m2-p4").textContent;

  return[
    player_r2_m1_p1,
    player_r2_m1_p2,
    player_r2_m2_p3,
    player_r2_m2_p4,
  ]
}

function DefinePlayersR2() {
  var players_name = GetPlayerNameR1();
  var players_score = GetPlayersScoreR1();
  if (players_score[0] > players_score[1]) {
    document.getElementById("player-r2-m1-p1").innerHTML = players_name[0]
  } else {
    document.getElementById("player-r2-m1-p1").innerHTML = players_name[1]
  }

  if (players_score[2] > players_score[3]) {
    document.getElementById("player-r2-m1-p2").innerHTML = players_name[2]
  } else {
    document.getElementById("player-r2-m1-p2").innerHTML = players_name[3]
  }

  if (players_score[4] > players_score[5]) {
    document.getElementById("player-r2-m2-p3").innerHTML = players_name[4]
  } else {
    document.getElementById("player-r2-m2-p3").innerHTML = players_name[5]
  }

  if (players_score[6] > players_score[7]) {
    document.getElementById("player-r2-m2-p4").innerHTML = players_name[6]
  } else {
    document.getElementById("player-r2-m2-p4").innerHTML = players_name[7]
  }

};

function DefinePlayersFinale() {
  var players_name = GetPlayerNameR2();
  var players_score = GetPlayersScoreR2();
  if (players_score[0] > players_score[1]) {
    document.getElementById("player-r3-m1-p1").innerHTML = players_name[0]
  } else {
    document.getElementById("player-r3-m1-p1").innerHTML = players_name[1]
  }

  if (players_score[2] > players_score[3]) {
    document.getElementById("player-r3-m1-p2").innerHTML = players_name[2]
  } else {
    document.getElementById("player-r3-m1-p2").innerHTML = players_name[3]
  }
}
