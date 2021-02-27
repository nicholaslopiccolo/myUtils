$(document).keydown(function(e){

    var el = document.getElementById("0");

    let coordsEl = el.getBoundingClientRect();



    switch(e.keyCode){

        // Left

        case 65:{

            $("#0").css({left: coordsEl.left-5});

            break;

        }

        // Up

        case 87:{

            console.log(coordsEl.y)

            $("#0").css({top: coordsEl.y+0.5});

            break;

        }

        // Right

        case 68:{

            $("#0").css({left: coordsEl.left+5});

            break;

        }

        // Down

        case 83:{

            console.log(coordsEl.y)

            $("#0").css({top: coordsEl.ys-0.5});

            break;

        }

    }

})
