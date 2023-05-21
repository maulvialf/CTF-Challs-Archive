from defusedxml import ElementTree
import urllib

def error_handler():
    def external_handler(parser, context, base, sysid, pubid):
        print('parser: {}\ncontext: {}\nbase: {}\nsysid: {}\npubid: {}\n'.format(
            parser, context, base, sysid, pubid))
        data = urllib.request.urlopen(sysid).read()
        child = parser.parser.ExternalEntityParserCreate(context)
        child.Parse(data)
        return 1

    d = ElementTree.DefusedXMLParser
    d.defused_entity_decl = None
    d.defused_unparsed_entity_decl = None
    d.defused_external_entity_ref_handler = external_handler