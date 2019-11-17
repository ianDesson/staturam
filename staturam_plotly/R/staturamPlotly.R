# AUTO GENERATED FILE - DO NOT EDIT

staturamPlotly <- function(id=NULL, label=NULL, value=NULL) {
    
    props <- list(id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StaturamPlotly',
        namespace = 'staturam_plotly',
        propNames = c('id', 'label', 'value'),
        package = 'staturamPlotly'
        )

    structure(component, class = c('dash_component', 'list'))
}
