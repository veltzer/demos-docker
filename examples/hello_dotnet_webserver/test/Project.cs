using GenHTTP.Api.Content;

using GenHTTP.Modules.IO;
using GenHTTP.Modules.Layouting;
using GenHTTP.Modules.Markdown;
using GenHTTP.Modules.Websites;

using GenHTTP.Themes.Lorahost;

namespace test
{

    public static class Project
    {

        public static IHandlerBuilder Create()
        {
            var theme = Theme.Create()
                             .Title("test")
                             .Subtitle("This is text.")
                             .Action("/section-1/", "Go to Section 1")
                             .Header(Resource.FromAssembly("header.jpg"));

            var menu = Menu.Empty()
                           .Add("{website}/", "Home")
                           .Add("section-1", "Section 1", new() { ("/sub/", "Sub Section") })
                           .Add("section-2", "Section 2")
                           .Add("about", "About");

            var website = Website.Create()
                                 .Theme(theme)
                                 .Menu(menu)
                                 .Content(GetContent())
                                 .AddScript("custom.js", Resource.FromAssembly("custom.js"))
                                 .AddStyle("custom.css", Resource.FromAssembly("custom.css"));

        return website;
        }

        public static IHandlerBuilder GetContent()
        {
            var resources = Resources.From(ResourceTree.FromAssembly("Static"));

            var section1 = Layout.Create()
                                 .Index(GetPage("Section1.Index.md", "Section 1"))
                                 .Add("sub", GetPage("Section1.Sub.md", "Sub Section"));

            var section2 = Layout.Create()
                                 .Index(GetPage("Section2.Index.md", "Section 2"));

            return Layout.Create()
                         .Index(GetPage("Home.md", "Home"))
                         .Add("section-1", section1)
                         .Add("section-2", section2)
                         .Add("about", GetPage("About.md", "About"))
                         .Add("static", resources);
        }

        private static IHandlerBuilder GetPage(string file, string title, string? description = null)
        {
            var page = ModMarkdown.Page(Resource.FromAssembly(file))
                                  .Title(title);

            if (description != null)
            {
                page.Description(description);
            }

            return page;
        }

    }

}
