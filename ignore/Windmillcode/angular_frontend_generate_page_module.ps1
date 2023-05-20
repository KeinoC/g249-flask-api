Param
(
    [Parameter(Mandatory = $true)] [string] $moduleName,
    [string]$moduleLocation="src/app/pages"
    [string]$routeName,
    [string]$componentName,
    [bool]$routing = $true,
    [string]$declaingModule ="../layouts/default",
    [bool]$flatModule = $true,

)


cd apps/zero/frontend/AngularApp/src




npx ng g @windmillcode/angular-templates:module
--name $moduleName
--routing=$routing
--route=$routeName
--module=$declaingModule
--flat=$flatModule
--component-name $componentName

# npx ng g @windmillcode/angular-templates:module --name blog --routing=true  --route=blog --module=../layouts/default --flat=false --component-name blog-main 
