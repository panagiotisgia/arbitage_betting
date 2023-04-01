query_over_under = """
        with a1 as (
        select nv.Team1, nv.Team2, 
        nv.O_odd as O_novibet, nv.U_odd as U_novibet, 
        stx.O_odd as O_stoiximan, stx.U_odd as U_stoiximan, 
        from football_novibet nv
        left join football_stoiximan stx on nv.Team1 = stx.Team1
        where nv.Over = 'O 2.5'
        ),
        a2 as (
        select nv.Team1, nv.Team2, 
        nv.O_odd as O_novibet, nv.U_odd as U_novibet, 
        stx.O_odd as O_stoiximan, stx.U_odd as U_stoiximan, 
        from football_novibet nv
        left join football_stoiximan stx on nv.Team2 = stx.Team2
        where nv.Over = 'O 2.5'
        ),
        a3 as (
        select * from a1 
        where a1.O_stoiximan <> 'No_bet' and a1.U_stoiximan <> 'No_bet'
        union all
        select * from a2
        where a2.O_stoiximan <> 'No_bet' and a2.U_stoiximan <> 'No_bet'
        ),
        a4 as (
        select a3.Team1, a3.Team2, 
        O_novibet, U_novibet, O_stoiximan, U_stoiximan,
        cast(case when O_novibet > O_stoiximan then O_novibet else O_stoiximan end as float) as O_max,
        cast(case when U_novibet > U_stoiximan then U_novibet else U_stoiximan end as float) as U_max
        from a3
        ),
        a5 as (
        select *, 1/O_max + 1/U_max as arb
        from a4 
        ),
        a6 as (
        select * from a5 
        where arb < 1 
        ),
        a7 as (
        select a6.*, nv.Team1 as Team1_novibet 
        from a6 
        left join football_novibet nv 
        on a6.Team1 = nv.Team1 
        and a6.O_novibet = nv.O_odd
        and a6.U_novibet = nv.U_odd
        ),
        a8 as (
        select a7.*, nv.Team2 as Team2_novibet 
        from a7 
        left join football_novibet nv 
        on a7.Team1 = nv.Team1 
        and a7.O_novibet = nv.O_odd
        and a7.U_novibet = nv.U_odd
        ),
        a9 as (
        select a8.*, stx.Team1 as Team1_stoiximan
        from a8 
        left join football_stoiximan as stx
        on a8.Team1 = stx.Team1 
        and a8.O_stoiximan = stx.O_odd
        and a8.U_stoiximan = stx.U_odd
        )
        select a9.*, stx.Team2 as Team2_stoiximan
        from a9
        left join football_stoiximan as stx
        on a9.Team2 = stx.Team2
        and a9.O_stoiximan = stx.O_odd
        and a9.U_stoiximan = stx.U_odd
        order by arb
"""


query_gg_ng = """
        with a1 as (
        select nv.Team1, nv.Team2, 
        nv.GG_odd as GG_novibet, nv.NG_odd as NG_novibet, 
        stx.GG_odd as GG_stoiximan, stx.NG_odd as NG_stoiximan, 
        from football_novibet nv
        left join football_stoiximan stx on nv.Team1 = stx.Team1
        where nv.GG <> 'Markets are not available'
        ),
        a2 as (
        select nv.Team1, nv.Team2, 
        nv.GG_odd as GG_novibet, nv.NG_odd as NG_novibet, 
        stx.GG_odd as GG_stoiximan, stx.NG_odd as NG_stoiximan, 
        from football_novibet nv
        left join football_stoiximan stx on nv.Team2 = stx.Team2
        where nv.GG <> 'Markets are not available'
        ),
        a3 as (
        select * from a1 
        where a1.GG_stoiximan <> 'No_bet' and a1.NG_stoiximan <> 'No_bet'
        union all
        select * from a2
        where a2.GG_stoiximan <> 'No_bet' and a2.NG_stoiximan <> 'No_bet'
        ),
        a4 as (
        select a3.Team1, a3.Team2, 
        GG_novibet, NG_novibet, GG_stoiximan, NG_stoiximan,
        cast(case when GG_novibet > GG_stoiximan then GG_novibet else GG_stoiximan end as float) as GG_max,
        cast(case when NG_novibet > NG_stoiximan then NG_novibet else NG_stoiximan end as float) as NG_max
        from a3
        ),
        a5 as (
        select *, 1/GG_max + 1/NG_max as arb
        from a4 
        ),
        a6 as (
        select * from a5 
        where arb < 1 
        ),
        a7 as (
        select a6.*, nv.Team1 as Team1_novibet 
        from a6 
        left join football_novibet nv 
        on a6.Team1 = nv.Team1 
        and a6.GG_novibet = nv.GG_odd
        and a6.NG_novibet = nv.NG_odd
        ),
        a8 as (
        select a7.*, nv.Team2 as Team2_novibet 
        from a7 
        left join football_novibet nv 
        on a7.Team1 = nv.Team1 
        and a7.GG_novibet = nv.GG_odd
        and a7.NG_novibet = nv.NG_odd
        ),
        a9 as (
        select a8.*, stx.Team1 as Team1_stoiximan
        from a8 
        left join football_stoiximan as stx
        on a8.Team1 = stx.Team1 
        and a8.GG_stoiximan = stx.GG_odd
        and a8.NG_stoiximan = stx.NG_odd
        )
        select a9.*, stx.Team2 as Team2_stoiximan
        from a9
        left join football_stoiximan as stx
        on a9.Team2 = stx.Team2
        and a9.GG_stoiximan = stx.GG_odd
        and a9.NG_stoiximan = stx.NG_odd
        order by arb
"""