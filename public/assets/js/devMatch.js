$(document).ready(function() {
  let pageAnsArr = [];
  let pageAnsObj = {};
  let name;
  let email;
  let tel;
  let field;
  let language;
  let exp;
  let color;
  let sleep;

  // function PageAnsObj1(name, email, tel) {
  //   this.name = name;
  //   this.email = email;
  //   this.tel = tel;
  // };

  // function PageAnsObj2(field, exp, color) {
  //   this.field = field;
  //   this.language = language;
  //   this.exp = exp;
  //   this.color = color;
  // };

  // function PageAnsObj3(sleep) {
  //   this.sleep = true;
  // };

  $("#nextFirst").on("click", function() {
    let name = $("#name").val().trim();
    let email = $("#email").val().trim();
    let tel = $("#tel").val().trim();
    // PageAnsObj1(name, email, tel);
  });

  $("#secondFirst").on("click", function() {
    let field = $("#field").val().trim();
    let language = $("#language").val().trim();
    let exp = $("#exp").val().trim();
    let color = $("#color").val().trim();
    // PageAnsObj2(field, language, exp, color);
  });

  $("#nextFinal").on("click", function() {
    let sleep = $("#sleep").val().trim();
    pageAnsObj = {
      name = name,
      email = email,
      tel = tel,
      field = field,
      language = language,
      exp = exp,
      color = color,
      sleep = sleep
    };

    // PageAnsObj3(sleep);
    pageAnsArr.push(pageAnsObj);
  });

  $("#submit").on("click", function() {
    // QUESTION: What does $.get do? What are the parameters it is expecting?
    axios.post("/api/", pageAnsArr)
      .then(function(data) {
        console.log(data);
        if (data) {
          $("#stats").show();
          $("#name").text(data.name);
          $("#role").text(data.role);
          $("#age").text(data.age);
          $("#force-points").text(data.forcePoints);
        }
        else {
          $("#name").text("The force is not strong with this one. Your character was not found.");
          $("#stats").hide();
        }

      })
  });
}) 