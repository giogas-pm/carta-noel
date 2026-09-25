-- Carta do Noel: dados da criança NUNCA vão pro servidor (ficam no aparelho). Aqui só "pedido X pago".
create table if not exists public.noel_pedidos (
  slug text primary key,
  unlocked boolean not null default true,
  valor numeric,
  payment_id text,
  created_at timestamptz not null default now()
);
create table if not exists public.noel_eventos (
  id uuid primary key default gen_random_uuid(),
  evento text not null, slug text, meta jsonb,
  created_at timestamptz not null default now()
);
alter table public.noel_pedidos enable row level security;
alter table public.noel_eventos enable row level security;
drop policy if exists noel_eventos_ins on public.noel_eventos;
create policy noel_eventos_ins on public.noel_eventos for insert to anon with check (char_length(evento) <= 40);
revoke all on public.noel_pedidos from anon;
revoke select, update, delete on public.noel_eventos from anon;
create or replace function public.noel_status(p_slug text) returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce((select unlocked from noel_pedidos where slug = p_slug), false)
$$;
revoke all on function public.noel_status(text) from public;
grant execute on function public.noel_status(text) to anon, authenticated;
