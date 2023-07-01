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
    maxBytes = int(cmd.maxBytes)
    intervals = cmd.intervals
    random_offsets = cmd.random_offsets
    buffor = cmd.buffor

    # Set up some default values for the simulation
	#Config::SetDefault ("ns3::OnOffApplication::PacketSize", UintegerValue (210));
	#Config::SetDefault ("ns3::OnOffApplication::DataRate", StringValue ("448kb/s"));

    print("Create Nodes")
    nodes = ns.network.NodeContainer()
    nodes.Create(5)

    n0n4 = ns.network.NodeContainer(nodes.Get(0), nodes.Get(4))
    n1n4 = ns.network.NodeContainer(nodes.Get(1), nodes.Get(4))
    n2n4 = ns.network.NodeContainer(nodes.Get(2), nodes.Get(4))
    n3n4 = ns.network.NodeContainer(nodes.Get(3), nodes.Get(4))

    #create stack on nodes
    print("Creating stack")
    stack = ns.internet.InternetStackHelper()
    stack.Install(nodes)

    #create channels without ips
    print("Creating channels")
    p2p = ns.point_to_point.PointToPointHelper()
    p2p.SetDeviceAttribute("DataRate", ns.core.StringValue ("10Mbps"))
    p2p.SetChannelAttribute("Delay", ns.core.StringValue ("0ms"))
    d0d4 = p2p.Install(n0n4)
    d1d4 = p2p.Install(n1n4)
    d2d4 = p2p.Install(n2n4)
    d3d4 = p2p.Install(n3n4)

    # ip adresses setup
    print("Assigning IP adresses")
    ipv4 = ns.internet.Ipv4AddressHelper()
    ipv4.SetBase(ns.network.Ipv4Address("10.0.1.1"), ns.network.Ipv4Mask("255.255.255.0"))
    i0i4 = ipv4.Assign(d0d4)
    ipv4.SetBase(ns.network.Ipv4Address("10.0.1.2"), ns.network.Ipv4Mask("255.255.255.0"))
    i1i4 = ipv4.Assign(d1d4)
    ipv4.SetBase(ns.network.Ipv4Address("10.0.1.3"), ns.network.Ipv4Mask("255.255.255.0"))
    i3i4 = ipv4.Assign(d2d4)
    ipv4.SetBase(ns.network.Ipv4Address("10.0.1.4"), ns.network.Ipv4Mask("255.255.255.0"))
    i4i4 = ipv4.Assign(d3d4)

    #Create router nodes, init route tables
    ns.internet.Ipv4GlobalRoutingHelper.PopulateRoutingTables()