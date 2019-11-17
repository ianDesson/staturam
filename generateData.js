const data = require("./values.json")['del-lado'];

const abajo = data.abajo;
const medio = data["en-medio"];
const arriba = data.arriba;

var metaAbajo = {
  left: {
    "leaning-angle-avg": 0,
    "shoulder-elbow-wrist-avg": 0,
    "hip-shoulder-elbow-avg": 0
  },
  right: {
    "leaning-angle-avg": 0,
    "shoulder-elbow-wrist-avg": 0,
    "hip-shoulder-elbow-avg": 0
  }
};
arriba.forEach(element => {
  if (element.left["leaning-angle"])
    metaAbajo.left["leaning-angle-avg"] += element.left["leaning-angle"];
  if (element.left['shoulder-elbow-wrist'])
    metaAbajo.left['shoulder-elbow-wrist-avg'] += element.left['shoulder-elbow-wrist'];
  if (element.left['hip-shoulder-elbow'])
    metaAbajo.left['hip-shoulder-elbow-avg'] += element.left['hip-shoulder-elbow'];
  
  if (element.right["leaning-angle"])
    metaAbajo.right["leaning-angle-avg"] += element.right["leaning-angle"];
  if (element.right['shoulder-elbow-wrist'])
    metaAbajo.right['shoulder-elbow-wrist-avg'] += element.right['shoulder-elbow-wrist'];
  if (element.right['hip-shoulder-elbow'])
    metaAbajo.right['hip-shoulder-elbow-avg'] += element.right['hip-shoulder-elbow'];
});
metaAbajo.left['leaning-angle-avg'] /= abajo.length;
metaAbajo.left['shoulder-elbow-wrist-avg'] /= abajo.length;
metaAbajo.left['hip-shoulder-elbow-avg'] /= abajo.length;
metaAbajo.right['leaning-angle-avg'] /= abajo.length;
metaAbajo.right['shoulder-elbow-wrist-avg'] /= abajo.length;
metaAbajo.right['hip-shoulder-elbow-avg'] /= abajo.length;

console.log(metaAbajo);