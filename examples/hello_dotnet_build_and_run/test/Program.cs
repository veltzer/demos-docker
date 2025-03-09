using GenHTTP.Engine;

using GenHTTP.Modules.Practices;

using test;

var project = Project.Create();

return Host.Create()
           .Handler(project)
           .Defaults()
           .Console()
#if DEBUG
           .Development()
#endif
           .Run();