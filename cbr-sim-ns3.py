import ns.code
import ns.point_to_point
import ns.internet
import ns.applications
import ns.network


def main (argv):

    cmd = ns.code.Commandline()
    cmd.tracing = True
    cmd.maxBytes = 0
    cmd.intervals = 0
    cmd.random_offsets = False
    cmd.buffor = 10
    cmd.AddValue("tracing", "Flag tracing enable/disable")
    cmd.AddValue("maxBytes", "Flag maxBytes")
    cmd.AddValue("intervals", "Flag intervals between packet sends")
    cmd.AddValue("random_offsets", "Flag random offsets enable/disable")
    cmd.AddValue("buffor", "Flag buffor size (default: 10)")

    tracing = cmd.tracing
    maxBytes = cmd.maxBytes
    intervals = cmd.intervals
    random_offsets = cmd.random_offsets
    buffor = cmd.buffor
    
    