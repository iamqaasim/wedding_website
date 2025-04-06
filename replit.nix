{pkgs}: {
  deps = [
    pkgs.python312Packages.bcrypt
    pkgs.python312Packages.pymongo
    pkgs.mongodb-5_0
    pkgs.python312Packages.flask-compress
  ];
}
